import json

from elasticsearch import Elasticsearch

es = Elasticsearch('awsx_test_01:9201')


def pretty(js):
    return json.dumps(js, indent=2)


def search():
    content = {"profile": True, "query": {"match_all": {}}}
    return es.search('*', body=content, request_timeout=10000)


if __name__ == '__main__':
    res = search()
    print(res)
    for key in res.keys():
        if key == 'profile':
            for key2 in res[key]:
                for key3 in res[key][key2]:
                    print(key3['id'].replace('[', '').split(']')[1])
                    print(key3['searches'][0]['query'][0]['time_in_nanos'])
