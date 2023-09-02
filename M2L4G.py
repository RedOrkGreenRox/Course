from tkinter import *
import pyautogui
from random import *
colors = ['black', 'gray', 'brown', 'red', 'orange', 'lime', 'green', 'cyan', 'navy',
          'magenta', 'purple', 'violet', 'pink']

test = Tk()
test.geometry('500x500')
test.title('Мячик')
test.resizable(width=False, height=False)
canvas = Canvas(test, height=500, width=500)
canvas.place(x=0, y=0)


class Ball:
    def __init__(self):
        self.a = 9.80665
        self.b = 1
        self.color = choice(colors)
        self.x = 500 / 2
        self.y = 500 / 2
        self.xspeed = 0
        self.yspeed = 1

    def motion(self):
        global abs_coord_x1, abs_coord_y1, abs_coord_x2, abs_coord_y2, mouse_speed, x1, y1, x2, y2
        if self.yspeed < 40 and self.b == 1:  # Ускорение свободного падения
            self.yspeed += self.a / 100
        elif self.b == -1:
            self.xspeed += self.a / 100
        else:
            pass
        self.y += self.yspeed
        self.x += self.xspeed
        try:  # Скорость курсора
            mouse_speed = 0
            x1 = test.winfo_pointerx()
            y1 = test.winfo_pointery()
            abs_coord_x1 = test.winfo_pointerx() - test.winfo_rootx()
            abs_coord_y1 = test.winfo_pointery() - test.winfo_rooty()
            mouse_speed = int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5) // 5
            if mouse_speed == 0:
                mouse_speed = 1
        except Exception:
            pass
        if ((abs_coord_x1 - self.x) ** 2 + (
                abs_coord_y1 - self.y) ** 2 <= 25 ** 2 and abs_coord_x1 - self.x >= 0 >= abs_coord_y1 - self.y):
            self.yspeed = self.yspeed // 4 + mouse_speed
            self.xspeed = -mouse_speed  # 1 четверть круга
        elif ((abs_coord_x1 - self.x) ** 2 + (
                abs_coord_y1 - self.y) ** 2 <= 25 ** 2 and abs_coord_x1 - self.x <= 0 >= abs_coord_y1 - self.y):
            self.yspeed = self.yspeed // 4 + mouse_speed
            self.xspeed = mouse_speed  # 2 четверть круга
        elif ((abs_coord_x1 - self.x) ** 2 + (
                abs_coord_y1 - self.y) ** 2 <= 25 ** 2 and abs_coord_x1 - self.x <= 0 <= abs_coord_y1 - self.y):
            self.yspeed -= mouse_speed
            self.xspeed += mouse_speed  # 3 четверть круга
        elif ((abs_coord_x1 - self.x) ** 2 + (
                abs_coord_y1 - self.y) ** 2 <= 25 ** 2 and abs_coord_x1 - self.x >= 0 <= abs_coord_y1 - self.y):
            self.yspeed -= mouse_speed
            self.xspeed -= mouse_speed  # 4 четверть круга
        if self.y >= 475:  # Отскок от нижнего края.
            if self.yspeed > 1:
                self.yspeed = -self.yspeed // 2
            else:
                self.yspeed = -0.1
            self.y += self.yspeed
        if self.y <= 25:  # Отскок от верхнего края
            self.yspeed = -self.yspeed // 2
            self.y += self.yspeed
        if self.x >= 475:  # Отскок от правой стены
            self.xspeed = -self.xspeed // 2
            self.x += self.xspeed
        if self.x <= 25 and self.xspeed < 0:  # Отскок от левой стены
            self.xspeed = -self.xspeed // 2
            self.x += self.xspeed
        # print(self.xspeed, self.yspeed)
        x2 = test.winfo_pointerx()
        y2 = test.winfo_pointery()

    @staticmethod
    def reverse__(event):
        if ball.b != 0:
            ball.b = 0
        else:
            ball.b = 1

    @staticmethod
    def reverse_(event):
        ball.b = -1

    @staticmethod
    def reverse(event):
        ball.a = -ball.a

    @staticmethod
    def map(event):
        ball.xspeed += -randint(-10, 10)
        ball.yspeed += -randint(-10, 10)

    @staticmethod
    def unmap(event):
        ball.xspeed, ball.yspeed = 0, 0
        ball.color = choice(colors)

    @staticmethod
    def drag(event):
        global x, y, _x, _y
        try:
            _x, _y = x, y
        except Exception:
            pass
        x, y = event.x + ball.x, event.y + ball.y
        try:
            ball.xspeed += (_x - x)
            ball.yspeed += (_y - y)
        except Exception:
            pass
        _x, _y = x, y


ball = Ball()


def game():
    canvas.delete('all')
    canvas.create_oval(ball.x - 25, ball.y - 25, ball.x + 25, ball.y + 25, fill=ball.color, outline=ball.color,
                       tags='ball')
    canvas.create_text(ball.x, ball.y, text=int(abs((ball.xspeed + ball.yspeed) / 2)), font='Arial24', fill='snow')
    ball.motion()
    test.after(10, game)


game()
test.bind('<Map>', ball.map)
test.bind('<Unmap>', ball.unmap)
test.bind('<Configure>', ball.drag)
test.bind('<Button-1>', ball.reverse)
test.bind('<Button-2>', ball.reverse__)
test.bind('<Button-3>', ball.reverse_)
test.mainloop()
