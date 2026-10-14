import pickle


class Book_class:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = ""

    def create_book(self):
        self.book_id = input("Enter book id: ")
        self.book_title = input("Enter book title: ")
        self.author_id = input("Enter author id: ")
        self.publisher = input("Enter publisher: ")
        self.year_of_publication = input("Enter year of publication: ")

    def display_book(self):
        print("Book ID: " + self.book_id)
        print("Book title: " + self.book_title)
        print("Author ID: " + self.author_id)
        print("Publisher: " + self.publisher)
        print("Year of publication: " + self.year_of_publication)

class Author_class:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.emailid = ""

    def create_author(self):
        self.author_id = input("Enter author id: ")
        self.author_name = input("Enter author name: ")
        self.affiliation = input("Enter affiliation: ")
        self.country = input("Enter country: ")
        self.phone = input("Enter phone: ")
        self.emailid = input("Enter emailid: ")

    def display_author(self):
        print("Author ID: " + self.author_id)
        print("Author name: " + self.author_name)
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
        self.user_id = input("Enter user id: ")
        self.name = input("Enter user name: ")
        self.password = input("Enter password: ")
        self.address = input("Enter address: ")
        self.phone = input("Enter phone: ")
        self.emailid = input("Enter emailid: ")

    def display_user(self):
        print("User ID: " + self.user_id)
        print("Name: " + self.name)
        print("Password: " + self.password)
        print("Address: " + self.address)
        print("Phone: " + self.phone)
        print("Emailid : " + self.emailid)

def add_book():
    book = Book_class()
    book.create_book()
    book_file = open("myBooks.dat", "ab")
    pickle.dump(book, book_file)
    book_file.close()

def add_author():
    author = Author_class()
    author.create_author()
    author_file = open("myAuthors.dat", "ab")
    pickle.dump(author, author_file)
    author_file.close()

def add_user():
    user = User_class()
    user.create_user()
    user_file = open("myUsers.dat", "ab")
    pickle.dump(user, user_file)
    user_file.close()

def display_books():
    book_file2 = open("myBooks.dat", "rb")

    while(1):
        try:
            data = pickle.load(book_file2)
            print(data.book_id)
            print(data.book_title)
            print(data.author_id)
            print(data.publisher)
            print(data.year_of_publication)

        except (EOFError):
            break
    book_file2.close()


def display_authors():
    author_file2 = open("myAuthors.dat", "rb")

    while (1):
        try:
            data = pickle.load(author_file2)
            print(data.author_id)
            print(data.author_name)
            print(data.affiliation)
            print(data.country)
            print(data.phone)
            print(data.emailid)

        except (EOFError):
            break
    author_file2.close()

            
def display_users():


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
