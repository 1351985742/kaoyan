import socket
_original_getaddrinfo=socket.getaddrinfo
def _mineru_dns(host,port,*args,**kwargs):
 if host=='cdn-mineru.openxlab.org.cn': host='8.222.80.133'
 return _original_getaddrinfo(host,port,*args,**kwargs)
socket.getaddrinfo=_mineru_dns
from pathlib import Path
import sys,json,time
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

root=Path('/Users/devilrecal/Movies')
out=Path(__file__).resolve().parent
files=sorted(p for p in root.glob('*') if p.is_file() and p.suffix.lower() in {'.png','.jpg','.jpeg'} and out not in p.parents)
manifest=out/'manifest.json'
config=m.load_config(None)
session=m.requests.Session(); session.trust_env=False
proxy_session=m.requests.Session()
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
for ses in (session,proxy_session):
 ses.mount('https://',HTTPAdapter(max_retries=Retry(total=4,backoff_factor=2,status_forcelist=[429,500,502,503,504])))
normal_get=session.get
def routed_get(url,**kwargs):
 if 'cdn-mineru' in url: return proxy_session.get(url,**kwargs)
 return normal_get(url,**kwargs)
session.get=routed_get
m.requests=session
if manifest.exists():
    data=json.loads(manifest.read_text())
    batch=data['batch_id']
else:
    batch,urls=m.request_upload_urls(files,config,'vlm')
    data={'batch_id':batch,'model':'vlm','files':[{'source':str(p),'name':p.name,'order':i} for i,p in enumerate(files,1)]}
    manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2))
    (out/'upload_urls.json').write_text(json.dumps(urls))
    (out/'upload_urls.json').chmod(0o600)
    print('Batch:',batch,flush=True)
    m.upload_files(files,urls)
results=m.wait_for_results(batch,config,10,7200)
# Keep service results locally for recovery, including download locations.
(out/'service_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
byorder={int(r['data_id'].rsplit('_',1)[-1]):r for r in results if r.get('data_id')}
index=['# 图片识别目录','',f'原始图片：{len(files)} 张；模型：MinerU VLM。','']
for item in data['files']:
    r=byorder.get(item['order'],{})
    item['state']=r.get('state','missing'); item['error']=r.get('err_msg')
    if r.get('state')!='done':
        continue
    slug=f"{item['order']:03d}_{Path(item['name']).stem}"
    raw=out/'02_mineru_raw'/slug
    md=out/'chapters'/f'{slug}.md'
    md.parent.mkdir(exist_ok=True)
    if m.find_markdown(raw) is None: m.download_and_extract(r['full_zip_url'],raw)
    original=m.find_markdown(raw)
    if original is None:
        item['error']='No Markdown';continue
    text,images=m.rewrite_markdown(original.read_text(),raw,original,md,out/'images',slug)
    md.write_text(text)
    item.update(markdown=str(md.relative_to(out)),characters=len(text.strip()),images=images)
    index.append(f"{item['order']}. [{Path(item['source']).relative_to(root)}](chapters/{md.name})")
manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2))
(out/'00_目录.md').write_text('\n'.join(index)+'\n')
print('Finished:',sum('markdown' in x for x in data['files']),'/',len(files),flush=True)
