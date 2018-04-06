import random
import string
from time import sleep

from elasticsearch import Elasticsearch, helpers
from datetime import datetime, timedelta

file = 'indexdata.csv'
es = Elasticsearch('localhost:9200')


def do_index(es_index):
    f = open(file)

    print('Indexing docs into: ' + es_index)

    docs = []
    for doc_id, line in enumerate(f):
        fields = line.rstrip().split(",")
        doc = {"_index": es_index, "_type": "log", "_id": doc_id + 11,
               "namae": fields[0], "date": fields[1], "passcode": fields[2], "date2": fields[3]}
        docs.append(doc)
        if len(docs) == 10000:
            res = helpers.bulk(es, docs)
            print(res)
            docs = []
    if len(docs) > 0:
        res = helpers.bulk(es, docs)
        print(res)
    print('Indexed to {}'.format(es_index))
    sleep(1)
    f.close()


def update_index_data():
    f = open(file, 'w')
    dt = datetime.now()
    rand_str = lambda n: ''.join([random.choice(string.ascii_lowercase) for i in range(n)])

    for val in range(0, 1):
        dt = dt - timedelta(1)
        dt2 = dt - timedelta(random.randint(-3, 3))
        f.write(rand_str(10) + ',' + str(dt.isoformat()) + ',' + str(val) + ',' + str(dt2.isoformat()) + '\n')
    f.close()


if __name__ == '__main__':
    update_index_data()
    for i in range(11, 30):
        do_index('x2018_02_' + str(i))
    es.indices.flush()
    print('Finished indexing at {}'.format(datetime.now()))
