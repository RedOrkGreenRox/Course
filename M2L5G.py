import random
import requests
from bs4 import BeautifulSoup
import os
count = 0
request = input("Введите запрос.")
url = f'https://yandex.ru/images/search?from=tabbar&text={request}&p={count}'
count = int(input('Количество картинок')) // 30 + 1
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition Yx GX)'


def get_link_img(url):
    response = requests.get(url, headers={'user_agent': f'{ua}'})
    soap = BeautifulSoup(response.content, "html.parser")
    print(soap)
    links = soap.find_all("img", class_="serp-item__thumb justifier__thumb")
    for link in links:
        print(len(links))
        link = link.get("src")
        linked = "https:" + str(link)
        name = random.random()
        p = requests.get(linked)
        try:
            os.mkdir(fr'C:\Users\User\PycharmProjects\pythonProject\Курс\Фото\{request}')
            print('Директория создана.')
        except FileExistsError:
            pass
        out = open(fr"Фото\{request}\{name}.jpg", "wb")
        out.write(p.content)
        print('Файл загружен.')
        out.close()


for i in range(count):
    get_link_img(url[:url.rfind('=') + 1] + str(i))
