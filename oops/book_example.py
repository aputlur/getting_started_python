class Book:
    # create empty class
    # pass
    # class variable
    # name = "Default"

    def __init__(self, name, num):
        self.name = name
        self.num = num

    # it's like toString()
    def __repr__(self):
        return repr((self.name, self.num))

    def increase_no_of_copies(self, how_much):
        self.num += how_much

    def decrease_copies(self, decrease):
        self.num -= decrease


# create instance of a class
book1 = Book('Unlimited Memory', 10)
book2 = Book('Python', 100)

book1.increase_no_of_copies(100)
book2.decrease_copies(2)

print(book1)
print(book2)
