command, c, operations = input('* / + -'), 0, ['*', '/', '+', '-']
try:
    a = int(input())
except ValueError:
    print('Вы ввели недопустимый тип данных!')
else:
    try:
        b = int(input())
    except ValueError:
        print('Вы ввели недопустимый тип данных!')
    else:
        if command in operations:
            if command == '+':
                print(a + b)
            elif command == '-':
                print(a - b)
            elif command == '*':
                print(a * b)
            elif command == '/':
                print(a / b)
        else:
            print('Вы ввели недопустимую операцию или оператор')
