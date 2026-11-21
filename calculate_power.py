asking_the_equation_symbol = input("Enter the operation (+, -, *, /): ")
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

if asking_the_equation_symbol == "+":
        result = number_1 + number_2
        print("The result of addition is:", result)
if asking_the_equation_symbol == "-":
        result = number_1 - number_2
        print("The result of subtraction is:", result)
if asking_the_equation_symbol == "*":
        result = number_1 * number_2
        print("The result of multiplication is:", result)
if asking_the_equation_symbol == "/":
        result = number_1 / number_2
        print("The result of division is:", result)