number1 = int(input("Enter number1: "))
operator = input("Enter the operator: ")
number2 = int(input("Enter number2: "))

if operator == "+":
    c = number1 + number2
elif operator == "-":
    c = number1 - number2
elif operator == "*":
    c = number1 * number2
elif operator == "/":
    c = number1 / number2

print(c)

