from datetime import datetime
from time import sleep

from elasticsearch import Elasticsearch
import json

xsiem = 'xsiem01:9201'
aws = 'awsx_test_01:9201'
local = 'localhost:9200'
local2 = 'localhost:9201'
es = Elasticsearch(local)
file = 'status.csv'


def pretty(js):
    return json.dumps(js, indent=2)


def delete(inds):
    for ind in inds.keys():
        print('Deleting {}'.format(ind))
        print(es.indices.delete(ind))


def show_indices():
    return es.indices.get_alias("*")


def mapping():
    return pretty(es.indices.get_mapping())


def template():
    return pretty(es.indices.get_template())


def count():
    return es.count()['count']


def diff(num, now, start):
    print(now)
    print(start)
    print(now - start)
    print(num)
    print(num / (now - start).seconds)


def calc(start_str):
    start = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
    last = 0
    while True:
        now = datetime.now()
        current = count()

        diff(current, now, start)
        if last > 0:
            print("Current EPS:")
            diff(current - last, now, last_time)
        last = current
        last_time = now
        sleep(60)


def status():
    return es.cluster.health()['status']


def record_status():
    f = open(file, 'w')
    f.write('dt,status' + '\n')
    while True:
        f.write(datetime.now().isoformat() + ',' + status() + '\n')
        f.flush()
        # sleep()


if __name__ == '__main__':
    print(delete(show_indices()))
    # print(mapping())
    # print(template())
    # print(show_indices().keys())?
    # calc("2018-03-16 13:22:35")
    # record_status()
    # print(count())
