import requests
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/250_лучших_фильмов_по_версии_IMDb'
responce = requests.get(url)
soup = BeautifulSoup(responce.content, 'lxml')
films = soup.find_all('tr')[1:]
for film in films:
    print(film.find_all('a')[0]['title'])
