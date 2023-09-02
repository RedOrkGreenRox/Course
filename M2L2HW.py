# -*- coding: utf8 -*
# https://web.telegram.org/k/#@llve_bot
import telebot
token = ''
botMyName = telebot.TeleBot(token)


@botMyName.message_handler(commands=['start', 'help'])
def start(message):
    botMyName.send_message(message.from_user.id, 'Привет! Меня зовут бот, я умею знакомиться, напиши слово - привет')


@botMyName.message_handler(content_types=['text'])
def get_messages(message):
    if message.text.lower() == 'привет':
        botMyName.send_message(message.from_user.id, 'Привет, напиши своё имя и мы сможем познакомиться!')
        botMyName.register_next_step_handler(message, get_surname)


def get_surname(message):
    global name
    name = message.text
    botMyName.send_message(message.from_user.id, 'А какая у тебя фамилия?')
    botMyName.register_next_step_handler(message, get_result)


def get_result(message):
    global surname
    surname = message.text
    botMyName.send_message(message.from_user.id, f'Тебя зовут {name} {surname}. Очень приятно познакомиться!')


botMyName.polling(none_stop=True, interval=0)
