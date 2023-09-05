#Abstraction & Encapsulation
"""
Library management system task
- Cx shoult be able to display all books in the library
- Handle the process when cx requests to borrow a book
- update library collection when cx returns a book
"""
#class - library
#layers of abstraction - display available book, lend book, add book
#class - cx
#layers of abstraction - request book, return book

class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBook(self):
        print()
        print('Available books:')
        for book in self.availableBooks:
            print(book)

    def lendBook(self,requestedBook):
        if requestedBook in self.availableBooks:
            print(f'You have borrowed the book {requestedBook}.')
            self.availableBooks.remove(requestedBook)
        else:
            print('The selected book is unavailable.')

    def addBook(self,returnedBook):
        self.availableBooks.append(returnedBook)
        print('You have returned the book.')

class Customer:

    def requestBook(self):
        print('Enter the name of the book you want to borrow : ')
        self.book = input()
        return self.book

    def returnBook(self):
        print('Enter the name of the book you want to return: ')
        self.book = input()
        return self.book


#creating objects
library = Library(['Harry Potter','Narnia','Tom Sawyer'])
customer = Customer()

#user interface
while True:
    print('Enter 1 to display available books.')
    print('Enter 2 to request for a book.')
    print('Enter 3 to return a book')
    print('Enter 4 to exit.')
    userChoice = int(input())
    if userChoice == 1:
        library.displayAvailableBook()
    elif userChoice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice == 4:
        quit()
