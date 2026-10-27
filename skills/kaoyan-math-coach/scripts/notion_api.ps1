<#
.SYNOPSIS
  Minimal Notion REST client used by the kaoyan-math-coach skill.

.DESCRIPTION
  Sends one authenticated Notion API request and prints the JSON response.
  The token is read from $env:NOTION_TOKEN or, failing that, from a per-user
  file outside the git repository (default: %USERPROFILE%\.dsh\notion-token.txt).

  The DSH workspace sandbox blocks outbound network, so this script only works
  in a run that has network access (full-access approval or an unrestricted
  session). It auto-detects a local HTTP proxy on 127.0.0.1:7897 when -Proxy
  is not supplied.

.EXAMPLE
  .\notion_api.ps1 -Path /v1/users/me

.EXAMPLE
  .\notion_api.ps1 -Method POST -Path /v1/data_sources/<id>/query -Body '{"page_size":5}'

.EXAMPLE
  .\notion_api.ps1 -Method POST -Path /v1/pages -BodyFile payload.json
#>
[CmdletBinding()]
param(
  [ValidateSet('GET', 'POST', 'PATCH', 'DELETE')]
  [string]$Method = 'GET',

  [Parameter(Mandatory = $true)]
  [string]$Path,

  [string]$Body,
  [string]$BodyFile,

  [string]$Proxy,
  [switch]$NoProxy,

  [string]$NotionVersion = '2025-09-03',

  [string]$TokenFile = (Join-Path $env:USERPROFILE '.dsh\notion-token.txt'),

  [switch]$Quiet
)

$ErrorActionPreference = 'Stop'

# --- token ---------------------------------------------------------------
$token = $env:NOTION_TOKEN
$tokenSource = 'env:NOTION_TOKEN'
if ([string]::IsNullOrWhiteSpace($token)) {
  if (Test-Path -LiteralPath $TokenFile) {
    $token = (Get-Content -LiteralPath $TokenFile -Raw).Trim()
    $tokenSource = $TokenFile
  }
}
if ([string]::IsNullOrWhiteSpace($token)) {
  throw "Notion token not found. Set `$env:NOTION_TOKEN or write the integration secret to $TokenFile"
}

# --- url -----------------------------------------------------------------
if (-not $Path.StartsWith('/')) { $Path = '/' + $Path }
$uri = 'https://api.notion.com' + $Path

# --- proxy ---------------------------------------------------------------
$proxyUri = $null
if ($NoProxy) {
  $proxyUri = $null
}
elseif ($Proxy) {
  $proxyUri = $Proxy
}
else {
  $client = New-Object System.Net.Sockets.TcpClient
  try {
    $ok = $client.ConnectAsync('127.0.0.1', 7897).Wait(400)
    if ($ok -and $client.Connected) { $proxyUri = 'http://127.0.0.1:7897' }
  }
  catch { }
  finally { $client.Dispose() }
}

# --- body ----------------------------------------------------------------
$bodyBytes = $null
if ($BodyFile) {
  if (-not (Test-Path -LiteralPath $BodyFile)) { throw "BodyFile not found: $BodyFile" }
  $bodyBytes = [System.IO.File]::ReadAllBytes((Resolve-Path -LiteralPath $BodyFile).Path)
}
elseif (-not [string]::IsNullOrEmpty($Body)) {
  $bodyBytes = [System.Text.Encoding]::UTF8.GetBytes($Body)
}

# --- request -------------------------------------------------------------
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$headers = @{
  'Authorization'   = "Bearer $token"
  'Notion-Version'  = $NotionVersion
  'Accept'          = 'application/json'
}

$request = @{
  Uri                = $uri
  Method             = $Method
  Headers            = $headers
  TimeoutSec         = 60
  UseBasicParsing    = $true
}
if ($bodyBytes) {
  $request['Body'] = $bodyBytes
  $request['ContentType'] = 'application/json; charset=utf-8'
}
if ($proxyUri) {
  $request['Proxy'] = $proxyUri
}

$status = 0
$text = ''
try {
  $resp = Invoke-WebRequest @request
  $status = [int]$resp.StatusCode
  $text = $resp.Content
}
catch {
  $err = $_.Exception
  if ($err.Response) {
    $status = [int]$err.Response.StatusCode
    try {
      $reader = New-Object System.IO.StreamReader($err.Response.GetResponseStream())
      $text = $reader.ReadToEnd()
      $reader.Dispose()
    }
    catch { $text = $err.Message }
  }
  else {
    Write-Host "TRANSPORT_ERROR token_source=$tokenSource proxy=$(if($proxyUri){$proxyUri}else{'-'})"
    Write-Host $err.Message
    exit 2
  }
}

if (-not $Quiet) {
  Write-Host "HTTP=$status token_source=$tokenSource proxy=$(if($proxyUri){$proxyUri}else{'-'})"
  Write-Host $text
}

if ($status -lt 200 -or $status -ge 300) { exit 1 }
exit 0
