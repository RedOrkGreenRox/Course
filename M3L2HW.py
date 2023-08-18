

def palindrom(stroke):  # Берем строку.
    stroke = stroke.lower()    # Переводим все символы строки в нижний регистр.
    if stroke == stroke[::-1]:  # stroke[::-1] делает срез с начала до конца, в обратном порядке.
        return True    # То есть, переворачивает строку. Если изначальная строка равна перевернутой,
    else:   # то есть является палиндромом, возвращаем True, иначе возвращаем False
        return False


print(palindrom(input()))   # Печатаем результат функции для нашей строки.
