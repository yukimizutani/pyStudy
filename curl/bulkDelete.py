import pycurl

for i in range(97,98):
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, 'http://admin:admin@xsiem01:8090/v1/rules/{}'.format(str(i)))
    curl.setopt(pycurl.CUSTOMREQUEST, 'DELETE')
    curl.perform()