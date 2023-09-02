from random import *
from tkinter import *

(dragons, dragon_to_kill, defeated_dragons, dragons_to_win, dragon_count, canvas, bg_photo, j) = \
    ([], -1, 0, 10, 0, Canvas(window := Tk(), height=(height := 600), width=(width := 600)), PhotoImage(file='Фон.png'),
     0)
window.geometry(f'{height}x{width}')
window.title('Драконоборец')
window.resizable(width=False, height=False)
canvas.pack()


class Knight:
    def __init__(self):
        self.knight_photo = PhotoImage(file='Рыцарь.png')  # Модель рыцаря.
        self.speed = 0  # Скорость, в начале равна нулю.
        self.x = 70  # Начальная координата рыцаря x.
        self.y = height // 2  # Начальная координата рыцаря y.

    def knight_stop(self, event):  # Остановка
        self.speed = 0

    def knight_up(self, event):  # Движение вверх
        self.speed = -3

    def knight_down(self, event):  # Движение вниз
        self.speed = 3


class Dragon:
    def __init__(self):
        self.dragon_photo = PhotoImage(file='Дракон.png')  # Моделька дракона.
        self.x = 750  # Начальная координата x дракона.
        self.y = randint(100, 500)  # Начальная координата y дракона.
        self.speed = -randint(1, 3)  # Начальная скорость дракона.


knight = Knight()


def game():
    global dragon_count, dragon_to_kill, defeated_dragons, dragons, j
    if j == 0:
        if defeated_dragons < dragons_to_win:
            canvas.delete('all')
            canvas.create_image(height // 2, width // 2, image=bg_photo)  # Фон
            canvas.create_image(knight.x, knight.y, image=knight.knight_photo)  # Рыцарь
            canvas.create_text(30, 30, text=f'{defeated_dragons} / {dragons_to_win}',
                               fill='black')  # Счётчик убитых драконов
            if dragon_count >= randint(250, 500):  # Создание драконов
                for i in range(1, randint(2, 5)):
                    dragon = Dragon()
                    canvas.create_image(750, randint(100, 500), image=dragon.dragon_photo)
                    dragons.append(dragon)
                dragon_count = 0
            else:
                dragon_count += 1
                if dragon_count % 250 == 0:
                    print(dragon_count)
            if knight.speed > 0 and knight.y <= height - 3:
                knight.y += knight.speed
            elif knight.speed < 0 and knight.y >= 3:
                knight.y += knight.speed
            elif knight.speed > 0 and knight.y > height - 3:
                knight.y = 0
            elif knight.speed < 0 and knight.y < 3:
                knight.y = height - 3
            for dragon in dragons:
                canvas.create_image(dragon.x, dragon.y, image=dragon.dragon_photo)
                current_dragon = dragons.index(dragon)
                dragon.x += dragon.speed
                if randint(1, 3) == 2:
                    dragon.speed = -randint(1, 3)
                if ((dragon.x - knight.x) ** 2) + ((dragon.y - knight.y) ** 2) <= 96 ** 2:
                    dragon_to_kill = current_dragon
                if dragon.x <= 0:
                    canvas.delete('all')
                    canvas.create_text(height // 2, width // 2, text='Вы мертвы.', font='Verdana 42', fill='red')
                    dragon_count, dragons, dragon_to_kill, defeated_dragons, j = 0, [], -1, 0, 5
                    break
            if dragon_to_kill >= 0:
                del dragons[dragon_to_kill]
                dragon_to_kill = -1
                defeated_dragons += 1
            if defeated_dragons >= dragons_to_win:
                canvas.delete('all')
                canvas.create_text(height // 2, width // 2, text='Вы победили!', font='Verdana 42', fill='gold')
                window.after(1, game)
            window.after(5, game)
        else:
            dragon_count, dragons, dragon_to_kill, defeated_dragons, j = 0, [], -1, 0, 5
    else:
        try:
            canvas.delete('timer')
        except Exception:
            pass
        finally:
            print(j)
            canvas.create_text(width // 2, height // 3, text=j, fill='black', tags='timer')
            j -= 1
            window.after(1000, game)


window.bind('<w>', knight.knight_up)
window.bind('<s>', knight.knight_down)
window.bind('<Key-Up>', knight.knight_up)
window.bind('<Key-Down>', knight.knight_down)
window.bind('<KeyRelease>', knight.knight_stop)
game()
window.mainloop()
