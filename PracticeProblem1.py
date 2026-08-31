print("Enter Employee Name:")
employee_name = input()

print("Enter Basic Pay:")
basic_pay = int(input())

print("Enter Deductions:")
deductions = int(input())

total_pay = basic_pay - deductions

print("The total pay for", employee_name, "is:", total_pay)