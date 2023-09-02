import requests
url = 'https://swapi.dev/api/'
responce = requests.get(url).json()

people_api = responce.get('people')

planets_api = responce.get('planets')

starships_api = responce.get('starships')


def check_people(url):
    for i in range(1, 6):
        responce = requests.get(f'{url}/{i}').json()
        print(f'NAME: {responce["name"]}\nHEIGHT: {responce["height"]}\nMASS: {responce["mass"]}\n')


def check_planet(url):
    for i in range(1, 6):
        responce = requests.get(f'{url}/{i}').json()
        print(f'NAME: {responce["name"]}\nDIAMETER: {responce["diameter"]}\nPOPULATION: {responce["population"]}\n')


check_planet(planets_api)