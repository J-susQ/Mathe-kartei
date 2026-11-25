import json, hashlib, re, sys
sys.path.insert(0,'.')
from l1 import L1; from l2 import L2; from l3 import L3
out=[]
for lvl,L in ((1,L1),(2,L2),(3,L3)):
    seen=set()
    for cd in L:
        key=(cd['name'] or cd['front'])
        h=hashlib.sha1(f"{lvl}|{cd['topic']}|{key}".encode()).hexdigest()[:8]
        assert h not in seen, key; seen.add(h)
        cd=dict(cd); cd['id']=f"{lvl}-{h}"; cd['lvl']=lvl
        out.append({k:v for k,v in cd.items() if v!=""})
json.dump(out,open('cards.json','w'),ensure_ascii=False,separators=(',',':'))
from collections import Counter
print(Counter(c['lvl'] for c in out), len(json.dumps(out,ensure_ascii=False)))
