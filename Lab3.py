# Write a menu driven program to implement the following functionalities:
# Create at least three objects for each Book_class, Author_class, and User_class.
# Define functions to add values to these attributes. Add display function to display objects of these classes.

class Book_class(self):
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


class Author_class(self):
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

class User_class(self):
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
    book_id = input("Enter Book ID: ")
    book_title = input("Enter Book Title: ")
    author_id = input("Enter Author ID: ")
    author_name = input("Enter Author Name: ")
    publisher = input("Enter Publisher: ")
    year_of_publication = input("Enter Year of Publication: ")

    books.append(Book_class(
        book_id, book_title, author_id, author_name, publisher, year_of_publication
    ))
    print("Books Added")

def add_author():
    author_id = input("Enter Author ID: ")
    author_name = input("Enter Author Name: ")
    affiliation = input("Enter Affiliation: ")
    country = input("Enter Country: ")
    phone = input("Enter Phone: ")
    emailid = input("Enter Emailid : ")

    authors.append(Author_class(
        author_id, author_name, affiliation, country, phone, emailid
    ))
    print("Authors Added")


def add_user():
    user_id = input("Enter User ID: ")
    name = input("Enter User Name: ")
    password = input("Enter Password: ")
    address = input("Enter Address: ")
    phone = input("Enter Phone: ")
    emailid = input("Enter Emailid : ")

    users.append(User_class(
        user_id, name, password, address, phone, emailid
    ))
    print("Users Added")

def 

while True:
    print("Library Management System")
    print("1. Add Book")
    print("2. Add Author")
    print("3. Add User")
    print("4. Display Books")
    print("5. Display Authors")
    print("6. Display Users")
    print("7. Add to Books Borrowed")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
    elif choice == "2":
    elif choice == "3":
    elif choice == "4":
    elif choice == "5":
    elif choice == "6":
    elif choice == "7":
    elif choice == "8":
    else:
