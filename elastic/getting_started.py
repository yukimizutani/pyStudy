from elasticsearch import Elasticsearch
import json

es = Elasticsearch("localhost:9200")


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


if __name__ == '__main__':
    print(delete(show_indices()))
    print(mapping())
    print(template())
