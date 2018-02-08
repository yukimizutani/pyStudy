import pycurl

for i in range(1, 1000001):
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, 'http://admin:admin@localhost:8090/v1/indexer')
    curl.setopt(pycurl.CUSTOMREQUEST, 'GET')
    curl.perform()
    # print(res)
    if i % 100 == 0:
        print('\nCurled {} times'.format(str(i)))
