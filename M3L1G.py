from random import randint
from tkinter import *
from datetime import datetime

world = Tk()
world.geometry('600x600')
canvas = Canvas(world, height=600, width=600)
canvas.pack()
aspect_names = ['Aer', 'Alienis', 'Alkimia', 'Aqua', 'Arbor', 'Auram', 'Bestia', 'Coralos', 'Corpus', 'Dreadia',
                'Exanimis', 'Fames', 'Fluctus', 'Gelum', 'Granum', 'Gula', 'Herba', 'Ignis', 'Infernum', 'Infernus'
                'Iter', 'Limus', 'Luna', 'Lux', 'MRU', 'Magneto', 'Metallum', 'Mortuus', 'Motus', 'Ordo', 'Perditio',
                'Permutatio', 'Potentia', 'Praecantatio', 'Radio', 'Sano', 'Saxum', 'Sol', 'Stellae', 'Superbia',
                'Tempestas', 'Tempus', 'Tenebrae', 'Terra', 'Tincturem', 'Vacuos', 'Venenum', 'Ventus', 'Victus',
                'Vinculum', 'Vitium', 'Vitreus', 'Volatus']


class Ventus:
    image = PhotoImage(file='Alchemy/Ventus.png').subsample(1, 1)


class Stellae:
    image = PhotoImage(file='Alchemy/Stellae.png').subsample(1, 1)


class Luna:
    image = PhotoImage(file='Alchemy/Luna.png').subsample(1, 1)


class Alkimia:
    image = PhotoImage(file='Alchemy/Alkimia.png').subsample(1, 1)


class MRU:
    image = PhotoImage(file='Alchemy/MRU.png').subsample(1, 1)


class Magneto:
    image = PhotoImage(file='Alchemy/Magneto.png').subsample(1, 1)


class Superbia:
    image = PhotoImage(file='Alchemy/Superbia.png').subsample(1, 1)


class Infernus:
    image = PhotoImage(file='Alchemy/Infernus.png').subsample(1, 1)


class Gula:
    image = PhotoImage(file='Alchemy/Gula.png').subsample(1, 1)


class Vitium:
    image = PhotoImage(file='Alchemy/Vitium.png').subsample(1, 1)


class Exanimis:
    image = PhotoImage(file='Alchemy/Examinis.png').subsample(1, 1)


class Corpus:
    image = PhotoImage(file='Alchemy/Corpus.png').subsample(1, 1)


class Auram:
    image = PhotoImage(file='Alchemy/Auram.png').subsample(1, 1)


class Arbor:
    image = PhotoImage(file='Alchemy/Arbor.png').subsample(1, 1)


class Alienis:
    image = PhotoImage(file='Alchemy/Alienis.png').subsample(1, 1)


class Infernum:
    image = PhotoImage(file='Alchemy/Infernum.png').subsample(1, 1)


class Fluctus:
    image = PhotoImage(file='Alchemy/Fluctus.png').subsample(1, 1)


class Sol:
    image = PhotoImage(file='Alchemy/Sol.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Vacuos):
            return Stellae()


class Tempus:
    image = PhotoImage(file='Alchemy/Tempus.png').subsample(1, 1)


class Radio:
    image = PhotoImage(file='Alchemy/Radio.png').subsample(1, 1)


class Tincturem:
    image = PhotoImage(file='Alchemy/Tincturem.png').subsample(1, 1)


class Dreadia:
    image = PhotoImage(file='Alchemy/Dreadia.png').subsample(1, 1)


class Coralos:
    image = PhotoImage(file='Alchemy/Coralos.png').subsample(1, 1)


class Volatus:
    image = PhotoImage(file='Alchemy/Volatus.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Vacuos):
            return Superbia()
        elif isinstance(other, Aer):
            return Ventus()


class Vinculum:
    image = PhotoImage(file='Alchemy/Vinculum.png').subsample(1, 1)


class Tenebrae:
    image = PhotoImage(file='Alchemy/Tenebrae.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Vacuos):
            return Alienis()
        elif isinstance(other, Terra):
            return Luna()


class Sano:
    image = PhotoImage(file='Alchemy/Sano.png').subsample(1, 1)


class Praecantatio:
    image = PhotoImage(file='Alchemy/Praecantatio.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Aer):
            return Auram()
        elif isinstance(other, Perditio):
            return Vitium()
        elif isinstance(other, Ignis):
            return Infernus()
        elif isinstance(other, Potentia):
            return MRU()
        elif isinstance(other, Aqua):
            return Alkimia()


class Mortuus:
    image = PhotoImage(file='Alchemy/Mortuus.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Ignis):
            return Infernum()
        elif isinstance(other, Bestia):
            return Corpus()
        elif isinstance(other, Motus):
            return Exanimis()
        elif isinstance(other, Victus):
            return Spiritus()


class Metallum:
    image = PhotoImage(file='Alchemy/Metallum.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Iter):
            return Magneto()


class Limus:
    image = PhotoImage(file='Alchemy/Limus.png').subsample(1, 1)


class Iter:
    image = PhotoImage(file='Alchemy/Iter.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Metallum):
            return Magneto()


class Granum:
    image = PhotoImage(file='Alchemy/Granum.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Terra):
            return Herba()


class Herba:
    image = PhotoImage(file='Alchemy/Herba.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Aer):
            return Arbor()


class Fames:
    image = PhotoImage(file='Alchemy/Fames.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Vacuos):
            return Gula()


class Bestia:
    image = PhotoImage(file='Alchemy/Bestia.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Mortuus):
            return Corpus()


class Saxum:
    image = PhotoImage(file='Alchemy/Saxum.png').subsample(1, 1)


class Vitreus:
    image = PhotoImage(file='Alchemy/Vitreus.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Terra):
            return Metallum()


class Victus:
    image = PhotoImage(file='Alchemy/Victus.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Motus):
            return Bestia()
        elif isinstance(other, Vacuos):
            return Fames()
        elif isinstance(other, Terra):
            return Granum()
        elif isinstance(other, Aqua):
            return Limus()
        elif isinstance(other, Perditio):
            return Mortuus()
        elif isinstance(other, Ordo):
            return Sano()
        elif isinstance(other, Lux):
            return Sol()
        elif isinstance(other, Mortuus):
            return Spiritus()


class Venenum:
    image = PhotoImage(file='Alchemy/Venenum.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Aqua):
            return Coralos()
        elif isinstance(other, Ignis):
            return Dreadia()


class Vacuos:
    image = PhotoImage(file='Alchemy/Vacuos.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Victus):
            return Fames()
        elif isinstance(other, Potentia):
            return Praecantatio()
        elif isinstance(other, Lux):
            return Tenebrae()
        elif isinstance(other, Ordo):
            return Tempus()
        elif isinstance(other, Ignis or Victus):
            return Sol()
        elif isinstance(other, Tenebrae):
            return Alienis()
        elif isinstance(other, Fames):
            return Gula()
        elif isinstance(other, Volatus):
            return Superbia()
        elif isinstance(other, Sol):
            return Stellae()


class Tempestas:
    image = PhotoImage(file='Alchemy/Tempestas.png').subsample(1, 1)


class Potentia:
    image = PhotoImage(file='Alchemy/Potentia.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Vacuos):
            return Praecantatio()
        elif isinstance(other, Lux):
            return Radio()
        elif isinstance(other, Praecantatio):
            return MRU()
        elif isinstance(other, Terra):
            return Metallum()


class Permutatio:
    image = PhotoImage(file='Alchemy/Permutatio.png').subsample(1, 1)


class Motus:
    image = PhotoImage(file='Alchemy/Motus.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Victus):
            return Bestia()
        elif isinstance(other, Terra):
            return Iter()
        elif isinstance(other, Perditio):
            return Vinculum()
        elif isinstance(other, Aer):
            return Volatus()
        elif isinstance(other, Aqua):
            return Fluctus()
        elif isinstance(other, Mortuus):
            return Exanimis()


class Lux:
    image = PhotoImage(file='Alchemy/Lux.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Vacuos):
            return Tenebrae()
        elif isinstance(other, Ordo):
            return Tincturem()
        elif isinstance(other, Potentia):
            return Radio()


class Gelum:
    image = PhotoImage(file='Alchemy/Gelum.png').subsample(1, 1)


class Perditio:
    image = PhotoImage(file='Alchemy/Perditio.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Ignis):
            return Gelum()
        elif isinstance(other, Ordo):
            return Permutatio()
        elif isinstance(other, Aer):
            return Vacuos()
        elif isinstance(other, Aqua):
            return Venenum()
        elif isinstance(other, Victus):
            return Mortuus()
        elif isinstance(other, Motus):
            return Vinculum()
        elif isinstance(other, Praecantatio):
            return Vitium()


class Ordo:
    image = PhotoImage(file='Alchemy/Ordo.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Aer):
            return Motus()
        elif isinstance(other, Perditio):
            return Permutatio()
        elif isinstance(other, Ignis):
            return Potentia()
        elif isinstance(other, Terra):
            return Vitreus()
        elif isinstance(other, Victus):
            return Sano()
        elif isinstance(other, Lux):
            return Tincturem()
        elif isinstance(other, Vacuos):
            return Tempus()


class Ignis:
    image = PhotoImage(file='Alchemy/Ignis.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Perditio):
            return Gelum()
        elif isinstance(other, Aer):
            return Lux()
        elif isinstance(other, Ordo):
            return Potentia()
        elif isinstance(other, Venenum):
            return Dreadia()
        elif isinstance(other, Lux):
            return Sol()
        elif isinstance(other, Mortuus):
            return Infernum()
        elif isinstance(other, Praecantatio):
            return Infernus()
        elif isinstance(other, Aqua):
            return Aer()
        elif isinstance(other, Terra):
            return Saxum()


class Aqua:
    image = PhotoImage(file='Alchemy/Aqua.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Aer):
            return Tempestas()
        elif isinstance(other, Perditio):
            return Venenum()
        elif isinstance(other, Terra):
            return Victus()
        elif isinstance(other, Victus):
            return Limus()
        elif isinstance(other, Venenum):
            return Coralos()
        elif isinstance(other, Motus):
            return Fluctus()
        elif isinstance(other, Praecantatio):
            return Alkimia()
        elif isinstance(other, Ignis):
            return Aer()


class Aer:
    image = PhotoImage(file='Alchemy/Aer.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Ignis):
            return Lux()
        elif isinstance(other, Ordo):
            return Motus()
        elif isinstance(other, Aqua):
            return Tempestas()
        elif isinstance(other, Perditio):
            return Vacuos()
        elif isinstance(other, Motus):
            return Volatus()
        elif isinstance(other, Herba):
            return Arbor()
        elif isinstance(other, Praecantatio):
            return Auram()
        elif isinstance(other, Aer or Volatus):
            return Ventus()


class Terra:
    image = PhotoImage(file='Alchemy/Terra.png').subsample(1, 1)

    def __add__(self, other):
        if isinstance(other, Aqua):
            return Victus()
        elif isinstance(other, Ordo):
            return Vitreus()
        elif isinstance(other, Terra or Ignis):
            return Saxum()
        elif isinstance(other, Victus or Granum):
            return Herba()
        elif isinstance(other, Motus):
            return Iter()
        elif isinstance(other, Vitreus or Potentia):
            return Metallum()
        elif isinstance(other, Tenebrae):
            return Luna()


elements = [Ignis(), Aqua(), Aer(), Terra(), Ordo(), Perditio()]
for element in elements:
    canvas.create_image(randint(60, 540), randint(60, 540), image=element.image)


def move(event):
    now = datetime.now()
    if now.second % 2 == 0 and now.microsecond > 990000:
        el = randint(1, 6)
        if el == 1:
            spawn_1(lambda: "")
        elif el == 2:
            spawn_2(lambda: "")
        elif el == 3:
            spawn_3(lambda: "")
        elif el == 4:
            spawn_4(lambda: "")
        elif el == 5:
            spawn_5(lambda: "")
        elif el == 6:
            spawn_6(lambda: "")
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(images_id) == 2:
        elem_id_1, elem_id_2 = images_id[0], images_id[1]
        element_1 = elements[elem_id_1 - 1]
        element_2 = elements[elem_id_2 - 1]
        try:
            new_element = element_1 + element_2
        except Exception:
            pass
        try:
            if new_element is not None:
                canvas.delete(elem_id_1, elem_id_2)
                canvas.create_image(event.x, event.y, image=new_element.image)
                elements.append(new_element)
        except Exception:
            pass
    try:
        canvas.coords(*images_id, event.x, event.y)
    except Exception:
        pass


def spawn_1(event):
    new_element = Ignis()
    canvas.create_image(randint(60, 540), randint(60, 540), image=Ignis.image)
    elements.append(new_element)


def spawn_2(event):
    new_element = Aqua()
    canvas.create_image(randint(60, 540), randint(60, 540), image=Aqua.image)
    elements.append(new_element)


def spawn_3(event):
    new_element = Perditio()
    canvas.create_image(randint(60, 540), randint(60, 540), image=Perditio.image)
    elements.append(new_element)


def spawn_4(event):
    new_element = Ordo()
    canvas.create_image(randint(60, 540), randint(60, 540), image=Ordo.image)
    elements.append(new_element)


def spawn_5(event):
    new_element = Terra()
    canvas.create_image(randint(60, 540), randint(60, 540), image=Terra.image)
    elements.append(new_element)


def spawn_6(event):
    new_element = Aer()
    canvas.create_image(randint(60, 540), randint(60, 540), image=Aer.image)
    elements.append(new_element)


def move_delete(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    for image_id in images_id:
        canvas.delete(image_id)


world.bind('<B1-Motion>', move)
world.bind('<B3-Motion>', move_delete)
world.bind('1', spawn_1)
world.bind('2', spawn_2)
world.bind('3', spawn_3)
world.bind('4', spawn_4)
world.bind('5', spawn_5)
world.bind('6', spawn_6)
world.mainloop()
