# Create an employee Payroll Management Using a Dictionary
# Develop a menu-driven Python program to manage employee payroll information using dictionary and functions

myEmployees = {}
i = 1

def add_employee():
    global i

    Name = input("Enter employee name: ")
    Basic_Pay = float(input("Enter Basic Pay: "))
    Allowance = float(input("Enter Allowance: "))
    Deductions = float(input("Enter Deductions: "))
    Taxes = float(input("Enter Taxes: "))
    Gross_Pay = Basic_Pay + Allowance
    Net_Pay = Gross_Pay - Deductions - Taxes
    myEmployees.update({"employee" + str(i): {"emp_Name": Name,
                                          "emp_BasicPay": Basic_Pay,
                                          "emp_Allowance": Allowance,
                                          "emp_Deductions": Deductions,
                                          "emp_Taxes": Taxes,
                                          "emp_GrossPay": Gross_Pay,
                                          "emp_Net_Pay": Net_Pay

                                          }
                     })
    i = i + 1
def delete_employee():
    remove_employee = input("Enter employee number to delete: ")
    del myEmployees["employee" +  remove_employee]

def modify_employee():
    modify_employee = input("Enter employee number to modify: ")

    new_Name = input("Enter employee name: ")
    new_Basic_Pay = float(input("Enter Basic Pay: "))
    new_Allowance = float(input("Enter Allowance: "))
    new_Deductions = float(input("Enter Deductions: "))
    new_Taxes = float(input("Enter Taxes: "))
    new_Gross_Pay = new_Basic_Pay + new_Allowance
    new_Net_Pay = new_Gross_Pay - new_Deductions - new_Taxes
    myEmployees.update({"employee" + modify_employee: {"emp_Name": new_Name,
                                              "emp_BasicPay": new_Basic_Pay,
                                              "emp_Allowance": new_Allowance,
                                              "emp_Deductions": new_Deductions,
                                              "emp_Taxes": new_Taxes,
                                              "emp_GrossPay": new_Gross_Pay,
                                              "emp_Net_Pay": new_Net_Pay

                                              }
                        })


def print_employees():
    print(myEmployees)
def exit_program():
    exit()

while True:
    print("1. Add an Employee: ")
    print("2. Delete an Employee: ")
    print("3. Modify an Employee: ")
    print("4. Display all Employees: ")
    print("5. Exit the Program")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        delete_employee()
    elif choice == "3":
        modify_employee()
    elif choice == "4":
        print_employees()
    elif choice == "5":
        exit_program()
    else:
        print("Please enter a valid choice")