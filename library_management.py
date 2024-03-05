# Library management app

class Book:
    def __init__(self, title = " ", copies=0):

        self.title = title
        self.copies = copies

    def __str__(self):
        return f"{self.title}, {self.copies}"
    

class User:

    def __init__(self, name, borrowed_books: list[Book], fines: int=0):
        self.name = name 
        self.borrowed_books = borrowed_books
        self.fines = fines
        
    def __str__(self):
        return f"{self.name}, {self.borrowed_books}, {self.fines}"


class Library:
    def __init__(self, books: list[Book], current_borrowers: list=[]):
        self.books = books
        self.current_borrowers = current_borrowers

    def __str__(self):
        return f"{[book.title for book in self.books]}, {self.current_borrowers}"

    def checkout_book(self, book_title, user: User):
        if isinstance(book_title, str) == False:
            raise TypeError("Book title must be a string")
               
        for book in self.books:
            if book_title == book.title:
                print(book_title)
                if book.copies > 0 and len(user.borrowed_books) < 3:
                    print(user.borrowed_books)
                    book.copies -= 1
                    self.current_borrowers.append(user)
                    user.borrowed_books.append(book)
                    break
                    
                else: 
                    print("The book is unavailable or the user has too many books borrowed")
            else:
                break
    
    def return_book(self, book_title:str, user:User):
        
        for book in user.borrowed_books:

            if book_title == book.title:
                book.copies += 1
                user.borrowed_books.remove(book)
                self.current_borrowers.remove(user)
                
                
            else:
                print("There is no such a title borrowed.")


book_1 = Book("Spellings", 3)
book_2 = Book("Japan", 2)
book_3 = Book("Geomap", 4)

user_1 = User("John", [], 0)
user_2 = User("Pete", [], 0)
user_3 = User("Jim", [], 1)

library_1 = Library([book_1, book_2, book_3], [])
users = [user_1, user_2, user_3]
print(library_1)

print("Welcome to the Library! \n")
user_name = input("Please enter your name :").capitalize()

def user_check(user_name):
    for user in users:
        if user.name == user_name:
            return user

user = user_check(user_name)        


action = input("Would you like to checkout the book? Y/N  :")
if action == "Y":
    title_checkout = input("Please enter the title you would like to checkout: ").capitalize()
    library_1.checkout_book(title_checkout, user)
else: 
    return_book = input("Please enter the title you would like to return: ").capitalize()
    fine_ind = int(input("Please enter '1' if this is a late return :"))
    if fine_ind == 1:
        user.fines +=1
    else:
        print("Thank you to timely return.")

    library_1.return_book(return_book, user)

print(user_1)
print(user_2)
print(user_3)

print(book_1)
print(book_2)
print(book_3)
