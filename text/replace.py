f = open('/home/yuki/xsiem/tesu.log')
out = open('/home/yuki/xsiem/tesuto.log', 'w')

for l in f:
    out.write(l.rstrip().replace('/', '-') + '\n')
out.close()
