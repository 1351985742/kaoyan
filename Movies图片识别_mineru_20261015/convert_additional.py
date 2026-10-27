from pathlib import Path
from PIL import Image
import sys,json,subprocess,tempfile,time
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,'/Users/devilrecal/mineru_agent_pipeline/tools')
import mineru_pipeline as m
out=Path(__file__).resolve().parent
root=Path('/Users/devilrecal/Movies')
meta=out/'additional_tiles.json'
if meta.exists():data=json.loads(meta.read_text())
else:
 data={'tiles':[]}
 for order,source in enumerate(sorted(root.glob('*.png')),1):
  with Image.open(source) as im:
   w,h=im.size
   if order not in {6,28}:continue
   # Contiguous pixel ranges cover the whole image exactly once.
   step=1600 if w>=2000 else 800
   for n,y in enumerate(range(0,h,step),1):
    tile=out/'01_upload_copies'/f'{order:03d}_{source.stem}_tile{n:02d}.jpg'
    im.crop((0,y,w,min(h,y+step))).convert('RGB').save(tile,quality=94,subsampling=0,optimize=True)
    data['tiles'].append({'source':str(source),'order':order,'tile':n,'y_start':y,'y_end':min(h,y+step),'upload':str(tile)})
 meta.write_text(json.dumps(data,ensure_ascii=False,indent=2))
files=[Path(t['upload']) for t in data['tiles']]
s=m.requests.Session();s.trust_env=False;m.requests=s
c=m.load_config(None)
if 'batch_id' not in data:
 batch,urls=m.request_upload_urls(files,c,'vlm');data['batch_id']=batch;data['upload_urls']=urls
 meta.write_text(json.dumps(data,ensure_ascii=False,indent=2));meta.chmod(0o600)
 for t,p,u in zip(data['tiles'],files,urls):
  if t.get('uploaded'):continue
  m.upload_files([p],[u]);t['uploaded']=True;meta.write_text(json.dumps(data,ensure_ascii=False,indent=2))
results=m.wait_for_results(data['batch_id'],c,10,7200)
(out/'additional_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
byname={r['file_name']:r for r in results}
def download(t):
 r=byname.get(Path(t['upload']).name,{})
 t['state']=r.get('state');t['error']=r.get('err_msg')
 if r.get('state')!='done':return
 raw=out/'02_mineru_raw_tiles'/Path(t['upload']).stem
 if m.find_markdown(raw) is None:
  with tempfile.TemporaryDirectory() as td:
   z=Path(td)/'result.zip'
   p=subprocess.run(['curl','-sSf','--retry','3','--resolve','cdn-mineru.openxlab.org.cn:443:8.222.80.133','--connect-timeout','15','--max-time','180','-o',str(z),r['full_zip_url']],capture_output=True)
   if p.returncode:t['error']='download failed';return
   m.safe_extract_zip(z.read_bytes(),raw)
 t['raw']=str(raw);print('分段已保存',Path(t['upload']).stem,flush=True)
with ThreadPoolExecutor(max_workers=6) as ex:list(ex.map(download,data['tiles']))
meta.write_text(json.dumps(data,ensure_ascii=False,indent=2))
print('长图分段完成',len(data['tiles']),flush=True)
