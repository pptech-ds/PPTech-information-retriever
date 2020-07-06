from rank_bm25 import BM25Okapi

dict_bm25ranker = {}

dict_bm25ranker['tokenized_corpus'] = [['les', 'oeufs', 'de', 'la', 'poule', 'frais', 'de', 'preference', 'Les', 'oeufs'], ['la', 'farine', 'de', 'ble', 'la', 'farine'], ['faire', 'des', 'crepes', 'cest', 'tout', 'un', 'art', 'bien', 'savoir', 'faire', 'des', 'crepes', 'necessite', 'du', 'rhum', 'Introduction', 'à', 'lart', 'de', 'faire', 'des', 'crêpes'], ['le', 'rhum', 'cest', 'bien', 'Le', 'rhum'], ['bien', 'melanger', 'la', 'farine', 'et', 'les', 'oeufs', 'le', 'mélangeage']]

dict_bm25ranker['tokenized_query'] = ['faire', 'crepes', 'crepe']

corpus = ['les oeufs de la poule frais de preference Les oeufs', 'la farine de ble la farine', 'faire des crepes cest tout un art bien savoir faire des crepes necessite du rhum Introduction à lart de faire des crêpes', 'le rhum cest bien Le rhum', 'bien melanger la farine et les oeufs le mélangeage']

dict_bm25ranker['bm25'] = BM25Okapi(dict_bm25ranker['tokenized_corpus'])
print('dict_bm25ranker[bm25]: {}\n'.format(dict_bm25ranker['bm25']))

dict_bm25ranker['doc_scores'] = dict_bm25ranker['bm25'].get_scores(dict_bm25ranker['tokenized_query'])
dict_bm25ranker['top_n'] = dict_bm25ranker['bm25'].get_top_n(dict_bm25ranker['tokenized_query'], corpus, n=100)

print('dict_bm25ranker[doc_scores]: {}\n'.format(dict_bm25ranker['doc_scores']))
print('dict_bm25ranker[top_n]: {}\n'.format(dict_bm25ranker['top_n']))