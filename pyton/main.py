import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKKEN = 'user token'
HEADER = {'Content-Type' : 'application/json','trainer_token':TOKKEN}
id = '######' # id pokemons


'''body_registration = {
    "trainer_token": TOKKEN,
    "email": "email user",
    "password": "password user"
}'''

body_create = {
    "name": "Veloceraptor",
    "photo_id": 6
} 

response_create = requests.post(url=f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json)
message = response_create.json() ['message']
print(message)


body_put = {
    "pokemon_id": id,
    "name": "Чармандер",
    "photo_id": 4
}

response_put = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response_put.json)

message = response_put.json() ['message']
print(message)

body_add_pokeball = {
    "pokemon_id": id
}


response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.json)
message = response_add_pokeball.json() ['message']
print(message)




'''pokemon_id = response_crate.json()['id']
print('id')
status_code=response_crate
if response_create.status_code == 201:
    print ('status 201 CREATED')'''


