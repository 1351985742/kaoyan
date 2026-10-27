from pathlib import Path
import sys,json,subprocess,tempfile
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,'/Users/devilrecal/mineru_agent_pipeline/tools')
import mineru_pipeline as m
out=Path(__file__).resolve().parent
rs=json.loads((out/'service_results.json').read_text())
def fetch(r):
 if r['state']!='done':return
 i=int(r['data_id'].rsplit('_',1)[1]);raw=out/'02_mineru_raw'/f'{i:03d}_{Path(r["file_name"]).stem}'
 if m.find_markdown(raw):return
 with tempfile.TemporaryDirectory() as td:
  p=Path(td)/'result.zip'
  run=subprocess.run(['curl','-sSf','--retry','3','--resolve','cdn-mineru.openxlab.org.cn:443:8.222.80.133','--connect-timeout','15','--max-time','180','-o',str(p),r['full_zip_url']],capture_output=True)
  if run.returncode: print('下载失败',i,flush=True);return
  m.safe_extract_zip(p.read_bytes(),raw)
 print('已保存',i,flush=True)
with ThreadPoolExecutor(max_workers=6) as ex:list(ex.map(fetch,rs))
