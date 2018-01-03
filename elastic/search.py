from elasticsearch import Elasticsearch

es = Elasticsearch('xsiem02:9200')

res = es.search('tesu4')
for key in res.keys():
    print(key)
    print(res[key])
