# Write a menu driven program to implement the following functionalities:
# Create at least three objects for each Book_class, Author_class, and User_class.
# Define functions to add values to these attributes. Add display function to display objects of these classes.

class Book_class:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = ""

    def create_book(self):
        self.book_id = input("Enter Book ID: ")
        self.book_title = input("Enter Book Title: ")
        self.author_id = input("Enter Author ID: ")
        self.publisher = input("Enter Publisher: ")
        self.year_of_publication = input("Enter Year of Publication: ")

    def display_book(self):
        print("Book ID: " + self.book_id)
        print("Book Title: " + self.book_title)
        print("Author ID: " + self.author_id)
        print("Publisher: " + self.publisher)
        print("Year of Publication: " + self.year_of_publication)


class Author_class:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.emailid = ""

    def create_author(self):
        self.author_id = input("Enter Author ID: ")
        self.author_name = input("Enter Author Name: ")
        self.affiliation = input("Enter Affiliation: ")
        self.country = input("Enter Country: ")
        self.phone = input("Enter Phone: ")
        self.emailid = input("Enter Emailid: ")

    def display_author(self):
        print("Author ID: " + self.author_id)
        print("Author Name: " + self.author_name)
        print("Affiliation: " + self.affiliation)
        print("Country: " + self.country)
        print("Phone: " + self.phone)
        print("Emailid: " + self.emailid)

class User_class:
    def __init__(self):
        self.user_id = ""
        self.name = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.emailid = ""

    def create_user(self):
        self.user_id = input("Enter User ID: ")
        self.name = input("Enter User Name: ")
        self.password = input("Enter Password: ")
        self.address = input("Enter Address: ")
        self.phone = input("Enter Phone: ")
        self.emailid = input("Enter Emailid : ")

    def display_user(self):
        print("User ID: " + self.user_id)
        print("Name: " + self.name)
        print("Password: " + self.password)
        print("Address: " + self.address)
        print("Phone: " + self.phone)
        print("Emailid : " + self.emailid)

books = []
authors = []
users = []

def add_book():
    book = Book_class()
    book.create_book()
    books.append(book)
    print("Book Added")

def add_author():
    author = Author_class()
    author.create_author()
    authors.append(author)
    print("Author Added")

def add_user():
    user = User_class()
    user.create_user()
    users.append(user)
    print("User Added")

def display_books():
    if books:
        for book in books:
            book.display_book()
    else:
        print("No books available.")


def display_authors():
    if authors:
        for author in authors:
            author.display_author()
    else:
        print("No authors available.")

def display_users():
    if users:
        for user in users:
            user.display_user()
    else:
        print("No students available.")

while True:
    print("Library Management System")
    print("1. Add Book")
    print("2. Add Author")
    print("3. Add User")
    print("4. Display Books")
    print("5. Display Authors")
    print("6. Display Users")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        add_author()
    elif choice == "3":
        add_user()
    elif choice == "4":
        display_books()
    elif choice == "5":
        display_authors()
    elif choice == "6":
        display_users()
    elif choice == "7":
        print("Exiting Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
