def multiply(N, A, R):
    return N * A * R

Radius_of_circle = int(input("Please enter the radius of the circle: "))

print(Radius_of_circle, " * ", 2, "*", 3.14, " = ", multiply(Radius_of_circle, 2, 3.14))

print("The circumference of the circle is: ", multiply(Radius_of_circle, 2, 3.14))