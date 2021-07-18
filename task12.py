#task1
class Animal():
    def __init__(self,name):
        self.name = name
    def talk(self):
        raise NotImplementedError("Not implemented by sub class")
class Cat(Animal):
    def talk(self):
        print('Meow')
class Dog(Animal):
    def talk(self):
        print('Bark')
dog = Dog('Joku')
dog.talk()
cat = Cat('Mur')
cat.talk()

# task2


class Author():
    def __init__(self, name, country, birthday):
        self.birthday = birthday
        self.country = country
        self.name = name
        self.books = []


class Library():
    def __init__(self, name, ):
        self.name = name
        self.books = []
        self.authors = []
        a1 = Author('George', 'Uk', 1969)
        self.authors.append(a1)
        b1 =Book('Mayhem', 1999, a1)
        self.books.append(b1)
    def new_book( self):
        bookname = input('Input book name ').capitalize()
        bookyear = int(input('Input book year '))
        authorname = input('Input authors name ').capitalize()
        authorcountry = input('Input authors country ').capitalize()
        authoryear = int(input('Input authors birth year '))
        author = Author(authorname, authorcountry, authoryear)
        book = Book(bookname, bookyear, author)
        author.books.append(book.name)
        self.books.append(book)
        self.authors.append(author)

    def group_by_author(self):
        inp_author = input('Enter authors name ')
        book_list = []
        for book in self.books:
            if book.author.name == inp_author:
                book_list.append(book.name)
        return book_list

    def group_by_year(self):
        inp_year = int(input('Enter publishing year '))
        bookyear_list = []
        for years in self.books:
            if years.year == inp_year:
                bookyear_list.append(years.name)
        return bookyear_list

class Book():
    def __init__(self, name, year, author):
        self.author = author
        self.year = year
        self.name = name


library = Library('Oblastna library ')

choice = ''
while choice != 'Exit':
    choice = input("Add new book, search by author, search by year, exit ").capitalize()
    if choice == 'Add new book':
        library.new_book()

    if choice == 'Search by author':
        print(library.group_by_author())

    if choice == 'Search by year':
        print(library.group_by_year())

#




