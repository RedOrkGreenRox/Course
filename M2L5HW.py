import requests
import json
url = 'https://www.cbr-xml-daily.ru/daily_jsonp.js'
responce = requests.get(url)
data = json.loads(responce.text[responce.text.index('{'):responce.text.rindex('}') + 1])
for key, value in data['Valute'].items():   # Для валют из домашки
    if key == 'USD':
        print(f'Курс доллара США({key}): {value["Value"]} рублей')
    elif key == 'MDL':
        print(f'Курс молдавских леев({key}): {value["Value"]} рублей')
    elif key == 'AUD':
        print(f'Курс австралийского доллара({key}): {value["Value"]} рублей')
#
# valutes = input(f'Укажите нужные вам валюты из списка через пробел(* для всех):\n' # Для выбранных валют.
#                 f'{str([valute for valute in data["Valute"].keys()])[1:-1]}\n').split(' ')
# for key, value in data['Valute'].items():
#     if key in valutes or valutes[0] == '*':
#         print(f'Курс {key}: {value["Value"]} рублей')
