from elasticsearch import Elasticsearch, helpers

file = 'indexdata.csv'


def do_index(es_index):
    es = Elasticsearch('xsiem02:9200')
    f = open(file)

    print('Indexing docs into: ' + es_index)

    docs = []
    for doc_id, line in enumerate(f):
        fields = line.rstrip().split(",")
        doc = {"_index": es_index, "_type": "log", "_id": doc_id + 11, "passcode": fields[0]}
        docs.append(doc)
        if len(docs) == 1000:
            res = helpers.bulk(es, docs)
            print(res)
            docs = []
    if len(docs) > 0:
        res = helpers.bulk(es, docs)
        print(res)


def update_index_data():
    f = open(file, 'w')

    for val in range(0, 1000):
        f.write(str(val) + '\n')


if __name__ == '__main__':
    update_index_data()
    for i in range(0, 5):
        do_index('tesu' + str(i))
