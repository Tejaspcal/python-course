lineway = int(input("Enter the number of lines for the pattern: "))
nuber_munch = 1

print("The triangle pattern of numbers")
for i in range(1, lineway + 1):
    for j in range(1, i + 1):
        print(nuber_munch, end=' ')
        nuber_munch = nuber_munch + 1
    print()