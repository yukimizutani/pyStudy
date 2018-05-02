import re

f = open('4656.log', 'r')
regex = r'アクセス:\s+(.*)\s+'
lis = []
i = 0

for l in f:
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
