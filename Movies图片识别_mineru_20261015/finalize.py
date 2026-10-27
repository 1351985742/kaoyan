from pathlib import Path
import json,sys,re,hashlib
from collections import defaultdict
sys.path.insert(0,'/Users/devilrecal/mineru_agent_pipeline/tools')
import mineru_pipeline as m
out=Path(__file__).resolve().parent
sources=sorted(Path('/Users/devilrecal/Movies').glob('*.png'))
long=json.loads((out/'long_tiles.json').read_text())
long['tiles'].extend(json.loads((out/'additional_tiles.json').read_text())['tiles'])
groups=defaultdict(list)
for t in long['tiles']:groups[t['order']].append(t)
chapters=out/'chapters';chapters.mkdir(exist_ok=True)
manifest={'source_directory':'/Users/devilrecal/Movies','scope':'顶层图片，不含子目录','files':[]}
index=['# Movies 图片识别目录','','范围：Movies 顶层 28 张图片，不含子目录。','','长图分段转换后按像素顺序合并；复杂表格保留 HTML，以便呈现合并单元格。识别文字与数字仍需结合原图核验。','']
alltext=['# Movies 图片识别合并版','', '云端 OCR 结果，含复杂表格；原图是核对依据。','']
errors=[];counts=[]
for i,source in enumerate(sources,1):
 slug=f'{i:03d}_{source.stem}';md=chapters/f'{slug}.md';segments=[]
 if i in groups:
  tiles=sorted(groups[i],key=lambda t:t['tile'])
  for t in tiles:
   raw=Path(t.get('raw',str(out/'02_mineru_raw_tiles'/Path(t['upload']).stem)))
   f=m.find_markdown(raw)
   if not f:errors.append(f'{source.name} 分段 {t["tile"]} 缺失');continue
   text,imgs=m.rewrite_markdown(f.read_text(),raw,f,md,out/'images',Path(t['upload']).stem)
   segments.append(f'<!-- 原图像素 y={t["y_start"]}:{t["y_end"]} -->\n\n{text}')
 else:
  raw=out/'02_mineru_raw'/slug;f=m.find_markdown(raw)
  if not f:errors.append(f'{source.name} 结果缺失');continue
  text,imgs=m.rewrite_markdown(f.read_text(),raw,f,md,out/'images',slug);segments=[text]
 body='\n\n'.join(segments)
 title=next((line.strip().lstrip('# ').strip() for line in body.splitlines() if line.strip() and not line.startswith('<!--') and '<' not in line),source.stem)
 if len(title)>40:title=source.stem
 text=f'# {title}\n\n[查看原图]({source})\n\n'+body
 md.write_text(text)
 item={'order':i,'source':str(source),'markdown':str(md.relative_to(out)),'state':'done','tiles':len(segments),'characters':len(body),'table_rows':body.count('<tr>')}
 manifest['files'].append(item)
 index.append(f'{i}. [{title}](chapters/{md.name}) · {source.name}'+(f' · {len(segments)} 段' if len(segments)>1 else ''))
 alltext.extend([f'<a id="image-{i:03d}"></a>',text.replace('../images/','images/'),'\n---\n'])
 counts.append(f'| {i} | {source.name} | {len(segments)} | {len(body)} | {body.count("<tr>")} |')
 # Check only extracted local image links.
 for _,link in m.MARKDOWN_IMAGE_RE.findall(text):
  if not link.startswith(('http:','https:','data:','/')) and not (md.parent/m.clean_link_target(link)).exists():errors.append(f'{md.name} 图片链接缺失: {link}')
 for match in m.HTML_IMAGE_RE.finditer(text):
  link=match.group(2)
  if not link.startswith(('http:','https:','data:','/')) and not (md.parent/m.clean_link_target(link)).exists():errors.append(f'{md.name} HTML 图片缺失: {link}')
 if len(body.strip())<50:errors.append(f'{md.name} 内容过短')
(out/'00_目录.md').write_text('\n'.join(index)+'\n')
(out/'全部图片_合并.md').write_text('\n'.join(alltext))
manifest['validation_errors']=errors
(out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
hashes=defaultdict(list)
for s in sources:hashes[hashlib.sha256(s.read_bytes()).hexdigest()].append(s.name)
duplicates=[v for v in hashes.values() if len(v)>1]
report=['# 转换检查记录','',f'输入 28 张顶层 PNG；生成 {len(manifest["files"])} 份 Markdown。',f'分段补转图片 {len(groups)} 张，共 {sum(len(v) for v in groups.values())} 个连续像素分段；保留初次云端结果及补转记录。',f'文件、空内容及本地图片链接检查问题：{len(errors)}。','','## 识别限制','','- 抽查原图和输出，已发现并通过分段重转解决部分超长图尾部截断问题。','- 复杂表格有合并单元格、切段边界和跨行院校名称，不能把本次 OCR 当作逐格人工校对结果。','- 初次输出已发现部分专业代码前导零丢失、院系名称误识别等问题；原始 OCR 结果保留，不凭推测批量改写数字。','- 招生人数、考试科目和院校归属在用于择校前仍需对照原图复核。','','## 原图重复','','未发现字节完全相同的图片。' if not duplicates else '\n'.join('、'.join(v) for v in duplicates),'','## 文件检查明细','','| 序号 | 原图 | 转换段数 | 字符数 | HTML 表格行数 |','|---|---|---:|---:|---:|',*counts,'','## 检查问题','',*errors]
(out/'转换检查.md').write_text('\n'.join(report)+'\n')
print('生成文档',len(manifest['files']),'错误',errors,'长图',len(groups))
