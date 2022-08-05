from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
index_name='cities'

def print_total_cities(_es,_index_name):
    print("Total Cities:")
    print(_es.count(index=_index_name))

def get_input_city_population():
    _city = input("Enter the city to get the population: ")
    _new_population = input("Enter the updated population: ")
    return _city, _new_population

def get_elasticsearch_id(_es,_index_name,_matchdoc):
    citysearch = _es.search(index=_index_name, body=_matchdoc)
    current_population_id = citysearch["hits"]["hits"][0]["_id"]
    print(current_population_id)
    return current_population_id

def update_elasticsearch(_es,_index_name,_current_population_id,_updatedoc):
    doctype = "_doc"
    ret = _es.update(index=_index_name, doc_type=doctype, id=_current_population_id, body=_updatedoc)
    print ('Updated Record:', ret)
    return ret

if __name__ == '__main__':
    print_total_cities(es,index_name)    
    city, new_population = get_input_city_population()

    matchdoc = {'query': {'bool': {'must': [{'match': {'city': city}}]}}}
    body = {'query': {'bool': {'must': [{'match': {'city': city}}]}}}
    updatedoc = {
			'doc' : {
				'population': new_population
			}
		}


    current_population_id = get_elasticsearch_id(es,index_name,matchdoc)
    response = update_elasticsearch(es,index_name,current_population_id,updatedoc)
    print(response)

