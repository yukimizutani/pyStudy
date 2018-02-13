from elasticsearch import Elasticsearch

es = Elasticsearch('localhost:9200')

res = es.search('tesu*', sort='date')
for key in res.keys():
    print(key)
    print(res[key])
