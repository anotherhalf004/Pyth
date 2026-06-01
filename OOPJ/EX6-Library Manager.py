class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def add_book(self,book):
        self.books.append(book)
        self.no_of_books += 1

    def print_books(self):
        print(self.books)
    
    def num_books(self):
        # print(len(self.books))
        return self.no_of_books
    
b1 = Library()
b1.add_book("Harry Potter")
b1.add_book("Invincible")
b1.print_books()
b1.num_books