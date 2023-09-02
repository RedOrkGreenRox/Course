import speech_recognition as sr
r = sr.Recognizer()


def recognize_speech():
    with sr.Microphone(device_index=1) as source:
        print('Скажи что-нибудь: ')
        try:
            audio = r.listen(source, phrase_time_limit=5)   # Можете убрать лимит, если у вас он сам заканчивает
            # запись. У меня он просто вечно "слушает".
            text = r.recognize_google(audio, language='ru_RU')
            return text
        except sr.UnknownValueError:
            return '*молчание*'
        except sr.RequestError as e:
            return f'Не распознанно:\n{e}'
            pass


while True:
    print(recognize_speech())
