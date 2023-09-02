from tkinter import *
tk = Tk()
tk.geometry('600x600')
tk.title('Котик')
canvas = Canvas(tk, height=600, width=600)
canvas.pack()


class Cat:
    def __init__(self, color1, color2, color3):
        self.main_color = color1
        self.nose_color = color2
        self.eyes_color = color3

    def create_cat_ears(self):
        canvas.create_polygon(100, 200, 150, 100, 200, 200, fill=self.main_color)
        canvas.create_polygon(400, 200, 450, 100, 500, 200, fill=self.main_color)

    def create_cat_face(self):
        canvas.create_rectangle(100, 200, 500, 500, fill=self.main_color)

    def create_cat_nose(self):
        canvas.create_polygon(250, 380, 350, 380, 300, 430, fill=self.nose_color)

    def create_cat_eyes(self):
        canvas.create_oval(150, 280, 200, 320, fill=self.eyes_color)
        canvas.create_oval(450, 280, 400, 320, fill=self.eyes_color)


# cat1 = Cat(input(), input(), input())
# cat1.create_cat_ears()
# cat1.create_cat_face()
# cat1.create_cat_nose()
# cat1.create_cat_eyes()
cat2 = Cat(input(), input(), input())
cat2.create_cat_ears()
cat2.create_cat_face()
cat2.create_cat_nose()
cat2.create_cat_eyes()
tk.mainloop()
