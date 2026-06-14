import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', encoding='utf-8') as f:
    c = f.read()

refs = re.findall(r'src="(Videos/[^"]+)"', c)
for r in refs:
    print(r)
