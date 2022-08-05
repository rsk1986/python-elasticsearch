from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

index_name='cities'

print("Total Cities:")
print(es.count(index=index_name))

city = input("Enter the city to get the population: ")

doc = {'query': {'bool': {'must': [{'match': {'city': city}}]}}}

def search_elasticsearch(_es,_index_name,_doc):
    citysearch = _es.search(index=_index_name, body=_doc)
    population = citysearch["hits"]["hits"][0]["_source"]["population"]
    return population

if __name__ == '__main__':
	response=search_elasticsearch(es,index_name,doc)
	print("Population is:", response)
