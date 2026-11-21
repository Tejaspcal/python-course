start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

squares = []
even_squares = []
odd_squares = []

for numbers in range(start, end + 1):
    squares1 = numbers ** 2
    squares.append(squares1)
    if numbers % 2 == 0:
        even_squares.append(squares1)
    else:
        odd_squares.append(squares1)

print("All squares:", squares)
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)
