from gtts import gTTS
from random import *
import pyaudio
import os
import speech_recognition as sr
# my_file = open('some.txt', 'r', encoding='utf-8')
# my_string = my_file.read()
# my_file.close()
# tts = gTTS(text=my_string, lang='ru')
# tts.save('some.mp3')

r = sr.Recognizer()
while True:
    try:
        with sr.Microphone(device_index=1) as source:
            print(f'Скажи что-нибудь... ({randint(1, 10)})')
            audio = r.listen(phrase_time_limit=5, source=source)
            speech = r.recognize_google(audio, language='ru_RU').lower()
            print(speech)
    except Exception as error:
        print(error)
        pass
