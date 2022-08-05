from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}]) 

def connect_elasticsearch(_es):
    if _es.ping():
        print('Elasticsearch is UP!')
    else:
        print('Elasticsearch is DOWN!')
    return _es

if __name__ == '__main__':
    status=connect_elasticsearch(es)



