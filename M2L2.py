# -*- coding: utf8 -*-
import telebot
import random
token = '6378962315:AAHfif_GSYVg_Bi7_7QiahE9NqppXYjiyQA'
bot = telebot.TeleBot(token)   # Подключение к боту.
#
#
# def my_decorator(func_to_decorate):
#     def decorated_func():   # Обёртка
#         print('Я пришел на работу!')    # Выполняется до функции
#         func_to_decorate()   # Сама функция
#         print('Я закончил работу!')    # Выполняется после функции
#     return decorated_func
#
# @my_decorator
# def my_func():
#     print('Я работаю!')
#
#
# my_func()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = f' Привет, {message.chat.first_name}! Я умею расскзаывать стихи,' \
                   ' знаю много интересных фактов и могу показывать милых котиков!'
    bot.send_message(message.chat.id, welcome_text)
    print(message)


@bot.message_handler(commands=['cat'])
def cats(message):
    cat_num = random.randint(1, 9)
    cat_image = open(f'img/{cat_num}.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_image)


@bot.message_handler(commands=['music'])
def send_music(message):
    muz = open('happy.mp3', 'rb')
    bot.send_audio(message.chat.id, muz)


bot.polling()
