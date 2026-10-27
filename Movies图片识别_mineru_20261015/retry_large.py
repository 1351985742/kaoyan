import socket
_original_getaddrinfo=socket.getaddrinfo
def _mineru_dns(host,port,*args,**kwargs):
 if host=='cdn-mineru.openxlab.org.cn': host='8.222.80.133'
 return _original_getaddrinfo(host,port,*args,**kwargs)
socket.getaddrinfo=_mineru_dns
from pathlib import Path
from PIL import Image
import sys,json
sys.path.insert(0,'/Users/devilrecal/mineru_agent_pipeline/tools')
import mineru_pipeline as m

import subprocess,tempfile
_original_download=m.download_and_extract
def _download_with_curl(url,target):
 print('[*] 下载结果:',target.name,flush=True)
 with tempfile.TemporaryDirectory() as td:
  z=Path(td)/'result.zip'
  result=subprocess.run(['curl','--silent','--show-error','--fail','--retry','3','--resolve','cdn-mineru.openxlab.org.cn:443:8.222.80.133','--connect-timeout','15','--max-time','180','-o',str(z),url],capture_output=True)
  if result.returncode: raise RuntimeError('Result download failed, curl code '+str(result.returncode))
  m.safe_extract_zip(z.read_bytes(),target)
m.download_and_extract=_download_with_curl

import requests
out=Path(__file__).resolve().parent
source=Path('/Users/devilrecal/Movies/mmexport1792065320031.png')
p=out/'01_upload_copies'/ (source.stem+'.jpg');p.parent.mkdir(exist_ok=True)
if not p.exists():
 with Image.open(source) as im:im.convert('RGB').save(p,quality=97,subsampling=0,optimize=True)
print('上传副本字节数',p.stat().st_size,flush=True)
s=requests.Session();s.trust_env=False
proxy=requests.Session()
get=s.get
s.get=lambda url,**kw:proxy.get(url,**kw) if 'cdn-mineru' in url else get(url,**kw)
m.requests=s
c=m.load_config(None)
f=out/'retry_batch.json'
if f.exists(): batch=json.loads(f.read_text())['batch_id']
else:
 batch,urls=m.request_upload_urls([p],c,'vlm');f.write_text(json.dumps({'batch_id':batch}))
 m.upload_files([p],urls)
r=m.wait_for_results(batch,c,10,7200)[0]
(out/'retry_result.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
if r['state']=='done':
 raw=out/'02_mineru_raw'/'003_mmexport1792065320031'
 m.download_and_extract(r['full_zip_url'],raw)
 print('补转完成',flush=True)
else: print(r.get('err_msg'),flush=True)
