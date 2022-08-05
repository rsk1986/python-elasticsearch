from operator import index
from random import random
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

index="cities"

city = input("Enter the city: ")
country = input("Enter the country: ")
population = input("Enter the population: ")
id=city+country

doc = {
    'city': city,
    'country': country,
    'population': population,
}

def insert_elasticsearch(_es,_index,_id,_doc):
	ret = _es.index(index=index, id=_id, body=_doc)
	return ret

if __name__ == '__main__':
	response=insert_elasticsearch(es,index,id,doc)
	print(response)





