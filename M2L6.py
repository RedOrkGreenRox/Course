import warnings
import requests
from bs4 import BeautifulSoup
from datetime import datetime
valuts = {}
now = str(datetime.now().strftime('%d/%m/%Y'))
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
date = f'?date_req={now}'
responce = requests.get(url + date)
xml = BeautifulSoup(responce.content, "lxml")
valutes = xml.find_all('valute')
for valute in valutes:
    valuts[valute.charcode.text] = [valute['id'], valute.nominal.text, valute.value.text]
    print(valute.name)
for valute in valuts:
    print(valute, valuts[valute])


def getCourse(id):
    return xml.find('valute', {'id': id}).value.text


print(getCourse("R01235"), "рублей за 1 доллар")
print(getCourse("R01239"), "рублей за 1 евро")
print(getCourse("R01375"), "рублей за 10 юаней")
