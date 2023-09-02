class Book:
    def __init__(self, information):
        self.title = information[:information.find(', ')]
        self.author = information[information.find(', ') + 2:information.rfind(', ')]
        self.year = information[information.rfind(', ') + 2:]

    def call(self):
        print(f'Название: {self.title}\nАвтор: {self.author}\nГод издания: {self.year}\n')


# book_1 = Book('Война и мир, Лев Толстой, 1869')
# book_2 = Book('Преступление и наказание, Фёдор Достоевский, 1866')
book_3 = Book(input('Название, автор, год издания\n'))
# book_1.call()
# book_2.call()
book_3.call()
