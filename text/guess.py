import codecs

import chardet

file = 'this/traceroute.txt'

f = open(file, 'rb')
encoding = chardet.detect(f.read())
print(encoding)
f.close()

f2 = codecs.open(file, 'r', encoding['encoding'])
for l in f2:
    print(l.rstrip())
f2.close()
