class Item:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __floordiv__(self, other):  # У меня нет обычного деления?
        # return self.num // other.num
        return int(self.num / other.num)


class Item2:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __floordiv__(self, other):  # У меня нет обычного деления?
        # return self.num // other.num
        return int(self.num / other.num)


item1 = Item(2)
item2 = Item2(2)
print(item1 + item2)
print(item1 - item2)
print(item1 * item2)
print(item1 // item2)   # Это НЕ деление нацело.
