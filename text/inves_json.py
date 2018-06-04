import re

f = open('4656.log', 'r')
f2 = open('del_4656.log', 'w')
regex = r'アクセス:\s+(.*)\s+'
lis = []
i = 0

for l in f:
    if 'DELETE' in l:
        f2.write(l.rstrip() + '\n')
    m = re.search(regex, l.rstrip())
    if 'DELETE' in m.group(1):
        print(m.group(1))
        i += 1
        # print(m.group(1))
        if not m.group(1) in lis:
            lis.append(m.group(1))
print(i)
for li in lis:
    print(li)
f.close()
f2.close()
