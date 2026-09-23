#menu-driven program: add, remove, edit, print, exit students dictionary
from os import name

students = {}
i = 1

while True:
    print("Please select one of the following: ")
    print("1. Add Student: ")
    print("2. Remove Student: ")
    print("3. Edit Student: ")
    print("4. Print Students: ")
    print("5. Exit")


    option = input("Enter your choice: ")

    if option == "1":
        name = input("Enter your name: ")
        major = input("Enter your major: ")
        year = input("Enter your year: ")

        students.update({"s"+str(i):
                            {
                            "stu_name":name,
                            "stu_major":major,
                            "stu_year":year
                            }
                        })
        i = i + 1
    elif option == "2":
        remove_student = input("Enter the number of the student you want to remove: ")
        del students["s" + remove_student]
    elif option == "3":
        edit_student = input("Enter the number of the student you want to edit: ")

        name = input("Enter your name: ")
        major = input("Enter your major: ")
        year = input("Enter your year: ")

        students.update({
            "s" + edit_student: {
                "stu_name": name,
                "stu_major": major,
                "stu_year": year
            }
        })
    elif option == "4":
        print(students)
    elif option == "5":
        print("Exiting Program")
        break
    else:
        print("N/A")