# Define the following classes:
# Customer(cid, cname, acc_no, balance, credit_card=[], transfer_funds(beneficiary_customer_object, amount))
# Card(card_no, cvv, expiry_date, balance)
# Write a menu-driven main program in Python to define these classes, and create at least 2
# objects for these two classes.
# The main menu should have:
# 1. Create Customer objects
# 2. Create Card objects
# 3. Transfer funds between customer objects
# 4. Assign card objects to customer objects
# 5. Display Customer Info
# 6. Display Card Info
# 7. Exit

import pickle


class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.balance = ""
        self.credit_card = []
        self.beneficiary_customer_object = ""
        self.amount = ""

    def create_customer(self):
        self.cid = input("Customer Id: ")
        self.cname = input("Customer Name: ")
        self.acc_no = input("Customer Account Number: ")
        self.balance = input("Customer Balance: ")
        self.credit_card = input("Customer Credit Card: ")
        self.beneficiary_customer_object = input("Customer Beneficiary Cost: ")
        self.amount = input("Customer Amount: ")

        customer.create_customer()
        customer_file = open("myCust.dat", "ab")
        pickle.dump(customer, customer_file)
        customer_file.close()

    def display_customer(self):
        print("Customer Id: " + self.cid)
        print("Customer Name: " + self.cname)
        print("Customer Account Number: " + self.acc_no)
        print("Balance: " + self.balance)
        print("Credit Card: " + self.credit_card)
        print("Beneficiary Cost Object: " + self.beneficiary_customer_object)
        print("Amount: " + self.amount)

        cust_file2 = open("myCust.dat", "rb")

        while (1):
            try:
                data = pickle.load(cust_file2)
                print(data.cid)
                print(data.cname)
                print(data.acc_no)
                print(data.balance)
                print(data.credit_card)
                print(data.beneficiary_customer_object)
                print(data.amount)

            except (EOFError):
                break
        cust_file2.close()

    def transfer_funds(self, beneficiary_customer_object, amount):


    def assign_card(self):



class Card:
    def __init__(self):
        self.card_no = ""
        self.cvv = ""
        self.expiry_date = ""
        self.balance = ""

    def create_card(self):
        self.credit_card = input("Customer Credit Card Number: ")
        self.cvv = input("Customer CVV: ")
        self.expiry_date = input("Customer Expiry Date: ")
        self.balance = input("Customer Balance: ")

        card.create_card()
        card_file = open("myCard.dat", "ab")
        pickle.dump(card, card_file)
        card_file.close()

    def display_card(self):
        print("Customer Credit Card Number: " + self.credit_card)
        print("Customer CVV: " + self.cvv)
        print("Customer Expiry Date: " + self.expiry_date)
        print("Balance: " + self.balance)

        card_file2 = open("myCard.dat", "rb")

        while (1):
            try:
                data = pickle.load(card_file2)
                print(data.credit_card)
                print(data.cvv)
                print(data.expiry_date)
                print(data.balance)

            except (EOFError):
                break
        card_file2.close()


while True:
    print("Choose one of the options below:")
    print("1. Create Customer")
    print("2. Create Card")
    print("3. Transfer funds between customer objects")
    print("4. Assign card objects to customer objects")
    print("5. Display Customer Info")
    print("6. Display Card Info")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

    elif choice == "2":

    elif choice == "3":

    elif choice == "4":

    elif choice == "5":

    elif choice == "6":

    elif choice == "7":
        print("Exiting Program.")
        break
    else:
        print("Invalid choice. Please try again.")
