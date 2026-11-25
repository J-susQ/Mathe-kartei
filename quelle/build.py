import re, base64, os, json
B=os.path.dirname(os.path.abspath(__file__)); K=os.path.join(B,'..','dl','package','dist')
tpl=open(os.path.join(B,'template.html')).read()
css=open(os.path.join(K,'katex.min.css')).read()
def font(m):
    name=m.group(1)
    data=base64.b64encode(open(os.path.join(K,'fonts',name+'.woff2'),'rb').read()).decode()
    return f'src:url(data:font/woff2;base64,{data}) format("woff2")'
css=re.sub(r'src:url\(fonts/([A-Za-z0-9_\-]+)\.woff2\) format\("woff2"\)(?:,url\([^)]*\) format\("[a-z]+"\))*',font,css)
assert 'fonts/' not in css, 'font replace failed'
cards=open(os.path.join(B,'cards.json')).read().replace('</','<\\/')
base=tpl.replace('/*KATEX_CSS*/',css).replace('/*CARDS*/',cards)
os.makedirs(os.path.join(B,'out','artifact'),exist_ok=True); os.makedirs(os.path.join(B,'out','pwa'),exist_ok=True)
art=base.replace('<!--KATEX_JS-->','<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>').replace('<!--PWA_HEAD-->','').replace('/*PWA_SW*/','')
open(os.path.join(B,'out','artifact','analysis-kartei.html'),'w').write(art)
kjs=open(os.path.join(K,'katex.min.js')).read().replace('</script','<\\/script')
head='<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icon-180.png"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="default"><meta name="apple-mobile-web-app-title" content="Analysis">'
reset='<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>'
pwa=base.replace('<!--KATEX_JS-->','<script>'+kjs+'</script>').replace('<!--PWA_HEAD-->',head+reset).replace('/*PWA_SW*/','if("serviceWorker" in navigator&&location.protocol==="https:")navigator.serviceWorker.register("sw.js").catch(function(){});')
pwa='<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'+pwa.replace('<div class="wrap"','</head><body><div class="wrap"',1)+'</body></html>'
open(os.path.join(B,'out','pwa','index.html'),'w').write(pwa)
json.dump({"name":"Analysis-Kartei","short_name":"Analysis","start_url":"./","scope":"./","display":"standalone","background_color":"#EEF1F5","theme_color":"#2445A8","lang":"de",
  "icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png","purpose":"any maskable"}]},
  open(os.path.join(B,'out','pwa','manifest.webmanifest'),'w'),ensure_ascii=False,indent=1)
open(os.path.join(B,'out','pwa','sw.js'),'w').write('''const C="analysis-kartei-v1";const F=["./","index.html","manifest.webmanifest","icon-180.png","icon-192.png","icon-512.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(F)).then(()=>self.skipWaiting()))});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==C).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener("fetch",e=>{if(e.request.method!=="GET")return;e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request).then(res=>{if(res.ok&&new URL(e.request.url).origin===location.origin){const cp=res.clone();caches.open(C).then(c=>c.put(e.request,cp))}return res}).catch(()=>caches.match("index.html"))))});
''')
from PIL import Image, ImageDraw, ImageFont
for sz in (180,192,512):
    im=Image.new('RGB',(sz,sz),'#2445A8'); d=ImageDraw.Draw(im)
    g=sz/12
    for i in range(1,12): d.line([(i*g,0),(i*g,sz)],fill='#2E52BC',width=max(1,sz//180)); d.line([(0,i*g),(sz,i*g)],fill='#2E52BC',width=max(1,sz//180))
    try: f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf',int(sz*.62))
    except Exception: f=ImageFont.load_default()
    d.text((sz/2,sz*.47),'∫',font=f,fill='white',anchor='mm')
    im.save(os.path.join(B,'out','pwa',f'icon-{sz}.png'))
print('artifact',len(art)//1024,'KB  pwa',len(pwa)//1024,'KB')
