
number = input().replace(' ', '')


def math(num):
    if '*' in num:
        multiplication(num)
    elif '/' in num:
        division(num)
    elif '+' in num:
        addition(num)
    elif '-' in num:
        substraction(num)


def multiplication(num):
    # print(num)
    # print(num[:num.find('*')])
    # print(num[num.find('*') + 1:])
    print(int(num[:num.find('*')]) * int(num[num.find('*') + 1:]))
    return str(int(num[:num.find('*')]) * int(num[num.find('*') + 1:]))


def division(num):
    # print(num)
    # print(num[:num.find('/')])
    # print(num[num.find('/') + 1:])
    print(int(int(num[:num.find('/')]) / int(num[num.find('/') + 1:])))
    return str(int(int(num[:num.find('/')]) / int(num[num.find('/') + 1:])))


def addition(num):
    # print(num)
    # print(num[:num.find('+')])
    # print(num[num.find('+') + 1:])
    print(int(int(num[:num.find('+')]) + int(num[num.find('+') + 1:])))
    return str(int(int(num[:num.find('+')]) + int(num[num.find('+') + 1:])))


def substraction(num):
    # print(num)
    # print(num[:num.find('-')])
    # print(num[num.find('-') + 1:])
    print(int(int(num[:num.find('-')]) - int(num[num.find('-') + 1:])))
    return str(int(int(num[:num.find('-')]) - int(num[num.find('-') + 1:])))


math(number)

