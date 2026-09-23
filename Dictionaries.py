myDict = {}
i = 1

while True:
    print("Please select one of the following: ")
    print("1. Add Current Course: ")
    print("2. Remove Current Course: ")
    print("3. Replace Current Course: ")
    print("4. Stop")


    option = input("Enter your choice: ")

    if option == "1":
        course_name = input("Enter a course name: ")
        myDict.update({"c_name"+str(i) : course_name})
        i = i + 1
        print(myDict)
    elif option == "2":
        remove_course = input("Enter the number of the course you want to remove: ")
        del myDict["c_name"+ remove_course]
        print(myDict)
    elif option == "3":
        replace_course = input("Enter the number of the course you want to replace: ")
        new_course = input("Enter the new course name: ")
        myDict.update({"c_name" + replace_course: new_course})
        print(myDict)
    elif option == "4":
        break
    else:
        print("N/A")