import time
from random import *
from tkinter import *
window = Tk()
window.geometry('500x400')
window.resizable(False, False)

color = 'green'
canvas = Canvas(window, width=500, height=400)
canvas.pack()


class Racket:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.line = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

    def left(self, event):
        self.x = -2

    def right(self, event):
        self.x = 2

    def draw(self):
        self.canvas.move(self.line, self.x, 0)
        pos = self.canvas.coords(self.line)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= 500:
            self.x = 0


class Ball:
    def __init__(self, canvas, racket, color):
        self.canvas = canvas
        self.timer = 0
        self.racket = racket
        self.myball = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.ball_list = [-3, -2, -1, 1, 2, 3]
        self.x = choice(self.ball_list)
        self.y = -1
        self.tch_btm = False

    def draw(self):
        self.canvas.move(self.myball, self.x, self.y)
        pos = self.canvas.coords(self.myball)
        timer = canvas.create_text(100, 100, text=self.timer, tags='timer')
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= 400:
            self.tch_btm = True
        if self.touch():
            self.y = -3
            canvas.delete('timer')
            self.timer += 1
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= 500:
            self.x = -3

    def touch(self):
        ball_pos = self.canvas.coords(self.myball)
        racket_pos = self.canvas.coords(self.racket.line)
        if ball_pos[2] >= racket_pos[0] and ball_pos[0] <= racket_pos[2]:
            if racket_pos[1] <= ball_pos[3] <= racket_pos[3]:
                return True
        return False


racket = Racket(canvas, color)
ball = Ball(canvas, racket, 'blue')

while True:
    if ball.tch_btm is False:
        ball.draw()
        racket.draw()
    else:
        canvas.create_text(500 // 2, 400 // 2, text='You lose!', font='Verdana 42', fill='red')
        break
    window.update()
    time.sleep(0.02)
window.mainloop()
