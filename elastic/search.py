from elasticsearch import Elasticsearch

es = Elasticsearch('localhost:9200')

res = es.search('tesu*', sort='date:desc')
for key in res.keys():
    print(key)
    print(res[key])
