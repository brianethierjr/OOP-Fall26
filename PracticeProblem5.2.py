#menu-driven program to add and delete students
from logging import PercentStyle

students = {}
n = 1

def add_student():
    Name = input("Enter student name: ")
    Lab1 = int(input("Enter grade for Lab 1: "))
    Lab2 = int(input("Enter grade for Lab 2: "))
    Lab3 = int(input("Enter grade for Lab 3: "))
    Lab4 = int(input("Enter grade for Lab 4: "))
    Lab5 = int(input("Enter grade for Lab 5: "))
    Total = (Lab1 + Lab2 + Lab3 + Lab4 + Lab5)
    Percent = (Total/50) * 100
    Average = (Total) / 5
    students.update({"student" + str(n):{"stu_name":Name,
                                    "stu_lab1":Lab1,
                                    "stu_lab2":Lab2,
                                    "stu_lab3":Lab3,
                                    "stu_lab4":Lab4,
                                    "stu_lab5":Lab5,
                                    "stu_total":Total,
                                    "stu_percent":Percent,
                                    "stu_average":Average
                                         }
                     })
    n = n + 1

def delete_student():
    remove_student = input("Enter student number to delete: ")
    del students["student" + remove_student]

def show_students():
    print(students)
def stop():
    exit()

while True:
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Display Students")
    print("4. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        add_student()
    elif option == "2":
        delete_student()
    elif option == "3":
        show_students()
    elif option == "4":
        stop()
    else:
        print("Invalid option")