from tkinter import *

window = Tk()
window.geometry('600x800')
window.title('Рисовака')
canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()


class Home:
    def __init__(self, number, roof_color, wall_color):
        self.number = number
        self.roof_color = roof_color
        self.wall_color = wall_color
        self.width = 140
        self.height = 130
        self.roof = None
        self.wall = None

    def build_house(self, x, y):
        h = self.height
        w = self.width
        self.roof = canvas.create_polygon(x, y, x + w, y, x + w / 2, h - 100, fill=self.roof_color)
        self.wall = canvas.create_rectangle(x + 20, y, x + 120, y + 100, fill=self.wall_color, outline='')


home1 = Home(1, 'gray', 'gray')
home1.build_house(50, 120)
home1.build_house(250, 160)
window.mainloop()
