import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKKEN = '49653b801ddd9ec018dded7208e940a6'
HEADER = {'Content-Type' : 'application/json','trainer_token':TOKKEN}
TRAINER_ID = '24791'
NAME = 'Эльф'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_name_trainer():
    response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Эльф'


