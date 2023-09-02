# print('\n'.join([str(I) for I in range(int(input('От: ')), int(input('До:')) + 1) if I % (n := int(input('Делиться на: ')) if 'n' not in globals() else n) == 0]))
from random import *

models = ['T-34', 'Tiger']
tanks = []
number = 1


class Tank:
    def __init__(self):
        global number
        self.id = number
        self.model = choice(models)
        if self.model == 'T-34':
            self.health = 100
        elif self.model == 'Tiger':
            self.health = 200
        if self.model == 'T-34':
            self.damage = randint(25, randint(25, 50))
        elif self.model == 'Tiger':
            self.damage = randint(30, randint(30, 40))
        if self.model == 'T-34':
            self.armor = 30
        elif self.model == 'Tiger':
            self.armor = 25
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


class NewYearTank(Tank):
    def __init__(self):
        super().__init__()
        self.frost_armor = True
        self.model = 'Новогодний Т-90'
        self.damage = randint(1, 100)
        self.armor = 0
        self.health = randint(100, 1000)

    def health_down(self, damage):
        super().health_down(damage // 2)

    def status(self):
        super().status()


for i in range(2):
    tanks.append(Tank())
    tanks[-1].status()
while tanks[0].health > 0 and tanks[1].health > 0:
    __import__('time').sleep(1)
    if tanks[0].health > 0:
        tanks[0].attack(tanks[1])
    if tanks[1].health > 0:
        tanks[1].attack(tanks[0])
