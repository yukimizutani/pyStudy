from elasticsearch import Elasticsearch

es = Elasticsearch('localhost:9200')


def add_repo():
    es.snapshot.create_repository('backup_loc', 'es_backup')


def create():
    es.snapshot.create('backup_loc', 'back')


if __name__ == '__main__':
    add_repo()
