import requests

es_index = 'movies' # equivalent to SQL database
es_type = '_doc' # equivalent to SQL table

data = {"director": "toto, Tim", "genre": ["Comedy","Sci-Fi"], "year": 1996, "actor": ["Jack Nicholson","Pierce Brosnan","Sarah Jessica Parker"], "title": "Mars Attacks!"}

res = requests.post('URLTEST', json=data)

# verification si l'authentification utilisateur a bien fonctionné
print(res.status_code)
if res.status_code != 200:
    print('request::request_from_db: Error, not connected during POST')
    exit(1)
else:
    print('element correctly added in es!')

res = requests.get('URLTEST')

print(res.status_code)
if res.status_code != 200:
    print('request::request_from_db: Error, not connected during GET')
    exit(1)
else:
    print('element correctly GET in es!')

res_json = res.json()
print(res_json)
