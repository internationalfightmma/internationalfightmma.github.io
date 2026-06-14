import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', encoding='utf-8') as f:
    c = f.read()

c = c.replace('Videos/camilo video.mov', 'Videos/camilo video.MOV')
c = c.replace('Videos/pablo 2.mov', 'Videos/pablo 2.MOV')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done')
