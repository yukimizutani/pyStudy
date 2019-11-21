import pycurl, json

pre = '{\"parameter\":\"'
mid = '\",\"mappedField\":\"'
post = '\"}'

requests = []

for i in range(0, 984):
    requests.append(pre + str(i) + mid + str(i) + post)

for i in range(985, 1000):
    requests.append(pre + str(i) + mid + "10" + post)

if __name__ == '__main__':
    c = pycurl.Curl()
    c.setopt(pycurl.HTTPHEADER, ["Content-type: application/json"])
    c.setopt(pycurl.USERPWD, 'admin:admin')
    c.setopt(pycurl.PROXY, 'localhost')
    c.setopt(pycurl.PROXYPORT, 8090)
    c.setopt(c.URL, 'http://admin:admin@localhost:8090/v1/receivers/3/import/add_mappings')
    data = '{\"mappings\":[' + ','.join(requests) + ']}'
    print(data)
    c.setopt(pycurl.CUSTOMREQUEST, 'PUT')
    c.setopt(pycurl.POSTFIELDS, data)
    res = c.perform()
    print(str(res))