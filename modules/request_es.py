import requests
import pandas as pd

from .functions import check_url


# requete de la base de données
def request_from_db(keywords_filter_list):
    es_index = 'discovery_dev' # equivalent to SQL database
    # es_type = '_doc' # equivalent to SQL table: mandatory to use _doc for text elements
    #keywords_list = 'crêpes'

    request_cmd_line = 'URLTEST/'+es_index+'/_search?q='+keywords_filter_list

    res = requests.get(request_cmd_line)

    # print(res.status_code)
    if res.status_code != 200:
        print('request_es::request_from_db: ERROR Elasticsearch requests.get({})'.format(request_cmd_line))
        exit(1)
    else:
        print('request_es::request_from_db: Elasticsearch requests.get({})'.format(request_cmd_line))

    res_json = res.json()
    # print(res_json)

    dict_result = {}
    dict_result['name'] = []
    dict_result['skill_id'] = []
    dict_result['knowledge_id'] = []
    dict_result['id'] = []
    dict_result['value'] = []
    dict_result['seed_url'] = []

    for i in range(len(res_json['hits']['hits'])):
        # print('name: {}'.format(res_json['hits']['hits'][i]['_source']['name']))
        # print('skill_id: {}'.format(res_json['hits']['hits'][i]['_source']['skill_id']))
        # print('knowledge_id: {}'.format(res_json['hits']['hits'][i]['_source']['knowledge_id']))
        # print('id: {}'.format(res_json['hits']['hits'][i]['_source']['id']))
        # print('value: {}'.format(res_json['hits']['hits'][i]['_source']['value']))
        # print('seed URL: {}\n\n'.format('URLTEST/'+str(res_json['hits']['hits'][i]['_source']['skill_id'])+'/knowledge/'+str(res_json['hits']['hits'][i]['_source']['knowledge_id'])+'/seed/'+str(res_json['hits']['hits'][i]['_source']['id'])))
        # print(res_json['hits']['hits'][i]['_source'])
        if(res_json['hits']['hits'][i]['_source']['id'] != ''):
            dict_result['name'].append(res_json['hits']['hits'][i]['_source']['name'])
            dict_result['skill_id'].append(res_json['hits']['hits'][i]['_source']['skill_id'])
            dict_result['knowledge_id'].append(res_json['hits']['hits'][i]['_source']['knowledge_id'])
            dict_result['id'].append(res_json['hits']['hits'][i]['_source']['id'])
            dict_result['value'].append(res_json['hits']['hits'][i]['_source']['value'])
            current_seed_url = 'URLTEST'+str(res_json['hits']['hits'][i]['_source']['skill_id'])+'/knowledge/'+str(res_json['hits']['hits'][i]['_source']['knowledge_id'])+'/seed/'+str(res_json['hits']['hits'][i]['_source']['id'])
            dict_result['seed_url'].append(current_seed_url)


    dict_result_filtered = {}
    dict_result_filtered['name'] = []
    dict_result_filtered['skill_id'] = []
    dict_result_filtered['knowledge_id'] = []
    dict_result_filtered['id'] = []
    dict_result_filtered['value'] = []
    dict_result_filtered['seed_url'] = []

    for i in range(len(dict_result['seed_url'])):
        # if(i==0):
        #     dict_result['seed_url'][i] = 'URLTEST'
        
        if(dict_result['seed_url'][i] not in dict_result_filtered['seed_url']):
            dict_result_filtered['name'].append(dict_result['name'][i])
            dict_result_filtered['skill_id'].append(dict_result['skill_id'][i])
            dict_result_filtered['knowledge_id'].append(dict_result['knowledge_id'][i])
            dict_result_filtered['id'].append(dict_result['id'][i])
            dict_result_filtered['value'].append(dict_result['value'][i])
            dict_result_filtered['seed_url'].append(dict_result['seed_url'][i])
                
    return dict_result_filtered



def gen_sentence_for_classifier(dict_es, query):
    dict_classifier = {}
    dict_classifier['sentence'] = []
    dict_classifier['label'] = []
    dict_classifier['seed_url'] = []

    # query_clean_tokens = tokenize_cleaned_text(clean_text(query))
    # query_clean = " ".join(query_clean_tokens)
    # print('gen_sentence_for_classifier: query: {}'.format(query))
    # print('gen_sentence_for_classifier: query_clean: {}\n'.format(query_clean))

    for i in range(len(dict_es['name'])):
        # print('\ngen_sentence_for_classifier: dict_es[value_clean][{}]: {}\n'.format(i, dict_es['value_clean'][i]))
        my_current_sentence = '[CLS] ' + query + ' [SEP] ' + dict_es['value'][i]
        dict_classifier['sentence'].append(my_current_sentence)
        dict_classifier['label'].append(0)
        dict_classifier['seed_url'].append(dict_es['seed_url'][i])

    df = pd.DataFrame(dict_classifier) 

    return df