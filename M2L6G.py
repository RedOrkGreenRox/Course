from datetime import datetime
from tkinter import *

import requests
from bs4 import BeautifulSoup

Courses = Tk()
Courses.geometry('500x400')
Courses.title('Курсы валют')
courses = Text()
courses.pack()


def values(event):
    courses.delete("1.0", END)
    now = str(datetime.now().strftime('%d/%m/%Y'))
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    date = f'?date_req={now}'
    responce = requests.get(url + date)
    xml = BeautifulSoup(responce.content, "lxml")
    valutes = xml.find_all('valute')
    for valute in valutes:
        courses.insert("1.0", f'{valute.value.text} Руб. за {valute.nominal.text} {valute.find("name").text}\n')


values(lambda event: 1)
Courses.bind('<KeyPress>', values)
Courses.bind('<ButtonPress>', values)
Courses.mainloop()
