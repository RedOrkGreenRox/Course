# print('\n'.join([str(I) for I in range(int(input('От: ')), int(input('До:')) + 1) if I % (n := int(input('Делиться на: ')) if 'n' not in globals() else n) == 0]))
from random import *
from tkinter import *
world = Tk()
world.geometry('500x500')
world.title('Танки?')
canvas = Canvas(world)
canvas.pack()
models = ['T-34', 'Tiger']
tanks = []
number = 1


class Tank:
    def __init__(self, model=choice(models)):
        global number
        self.id = number
        self.model = model
        if self.model == 'T-34':
            self.image = 'Танк1.png'
            self.x = randint(1, 500)
            self.y = randint(250, 500)
            self.health = 309
            self.armor = 20
            self.speed = 54
            self.damage = randint(19, randint(38, 76))
        elif self.model == 'Tiger':
            self.image = 'Танк2.png'
            self.x = randint(1, 500)
            self.y = randint(0, 250)
            self.health = 570
            self.armor = 28
            self.speed = 45.4
            self.damage = randint(22, randint(44, 88))
        number += 1

    def status(self):
        print(
            f'Номер: {self.id}\nМодель: {self.model}\nЗдоровье: {self.health}\nБроня: {self.armor}\nУрон: {self.damage}\n')

    def health_down(self, damage):
        self.health -= (damage - self.armor) if self.armor <= damage else 0
        print(f'Танк #{self.id}\nЗдоровье: {self.health}\n')

    def attack(self, enemy):
        if enemy.health <= 0 or enemy.health + enemy.armor <= self.damage:
            enemy.health = 0
            print(f'Экипаж танка #{enemy.id} уничтожен\n')
        else:
            if randint(1, 10) == 1:
                print(f'Танк #{self.id} промазал!\n')
            else:
                enemy.health_down(self.damage)
                print(f'Точно в цель, у танка #{enemy.id} осталось {enemy.health} здоровья\n')


for i in range(2):
    tanks.append(Tank(input(models)))
    tanks[-1].status()
while tanks[0].health > 0 and tanks[1].health > 0:
    __import__('time').sleep(1)
    canvas.delete('all')
    for tank in tanks:
        canvas.create_image(image=tank.image, x=tank.x, y=tank.y)
    if tanks[0].health > 0:
        tanks[0].move()
    if tanks[1].health > 0:
        tanks[1].move()
    world.mainloop()
