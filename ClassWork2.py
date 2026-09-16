#menu-driven Python program to implement the following operations

my_list = []  # create empty list

while True:
    print("Menu")
    print("1. Add number to the list: ") #add element to list
    print("2. Remove number from the list: ") #remove element from list
    print("3. Replace number from the list: ") #replace element from list
    print("4. Sort current list: ") #sort list
    print("5. Print current list") #print list
    print("6. Stop") #stop


    option = input("Enter your option: ")


    if option == "1":
        my_list.append(int(input("Enter a number: ")))
        print("Current list: ", my_list)

    elif option == "2":
        my_list.remove(int(input("Remove a number from the list: "))) #remove element from list

    elif option == "3":
        old_number = int(input("Enter the number you want to be replaced: "))
        new_number = int(input("Enter new number: "))

        index = 0
        for i in my_list:
            if i == old_number:
                break
        index = index + 1
        my_list[index] = new_number
        print("New list: ", my_list)

    elif option == "4": # sort elements in the list
        my_list.sort()
        print("Sorted list: ", my_list)

    elif option == "5": #finally print the list
        print("Current list: ", my_list)

    elif option == "6": #exit
        print("Exiting program")
        break
    else:
        print("N/A")





