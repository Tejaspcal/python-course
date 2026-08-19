print("Enter the marks obtained in 4 subjects:")
math = int(input("maths: "))
science = int(input("science: "))
history = int(input("history: "))
english = int(input("English: "))

sum = math + science + history + english
print("sum of math,science,history and english = ", sum)

total_grade = (sum / 400) * 100

print(end="Percentage Mark = ")
print(total_grade)