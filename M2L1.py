# -*- coding: utf8 -*-
num3, count = 0, 0
# first_var = 22  # int
# second_var = 3.14   # float
# third_var = 'Hello everyone'
# print(first_var + second_var)
# print(first_var - second_var)
# print(first_var * second_var)
# print(first_var / second_var)
# print(first_var ** second_var)
# print(first_var // second_var)
# print(first_var % second_var)
# print(str(first_var) + str(second_var))
# print(third_var + ' ! !')
# print(third_var * 20)
# print(type(first_var), type(second_var), type(third_var))
# print(third_var[-10::-1])
# if
# while True:
#     try:
#         num1 = int(input('Введите 1 число. '))
#         num2 = int(input('Введите 2 число. '))
#     except ValueError:
#         print('Неккоректное значение.')
#     else:
#         if num1 > num2:
#             print('Первое число больше второго.')
#         elif num1 < num2:
#             print('Первое число меньше второго. ')
#         else:
#             print('Числа равны.')
#     finally:
#         count += 1
#         print(f'{count} цикл завершен.')
# for
# for i in range(2, 7, 2):
#     print(i)
# Калькулятор.


def calc():
    global num1, num2, num3, count
    while True:
        print(f'\nРезультат прошлого вычисления: {num3}\nЦикл {count}')
        try:
            operation = input('Укажите интересующую вас операцию:\n"+" - сложение\n'
                              '"-" - вычитание\n"*" - умножение\n"/" - деление\n"**" - возведение в степень\n'
                              '"//" - целочисленное деление\n"%" - остаток от деления\n"&" - конкатенация чисел\n')
            num1, num2 = int(input('Первое число. ')), int(input('Второе число. '))
            num1 / num2
        except ValueError:
            print('Вы ввели не число!')
            count += 1
            next
        except ZeroDivisionError:
            print('Деление на ноль невозможно!')
            count += 1
            next
        else:
            if operation == '+':
                print('\n', num3 := num1 + num2)
                count += 1
                next
            elif operation == '-':
                print('\n', num3 := num1 - num2)
                count += 1
                next
            elif operation == '*':
                print('\n', num3 := num1 * num2)
                count += 1
                next
            elif operation == '/':
                print('\n', num3 := num1 / num2)
                count += 1
                next
            elif operation == '**':
                print('\n', num3 := num1 ** num2)
                count += 1
                next
            elif operation == '//':
                print('\n', num3 := num1 // num2)
                count += 1
                next
            elif operation == '%':
                print('\n', num3 := num1 % num2)
                count += 1
                next
            elif operation == '&':
                if input('Режим конкатенации строк Y/N') == 'Y':
                    num1, num2 = input('Первая строка: '), input('Вторая строка: ')
                print(num3 := str(num1) + str(num2))
                count += 1
                next
            else:
                print('Некорректная операция.')
                count += 1
                next



calc()
