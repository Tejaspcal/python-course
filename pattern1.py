print("Half of the pyramid  pattern of stars (*)")
Bagsofa = int(input("Enter the number of rows for the half pyramid: "))
for i in range(0, Bagsofa):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()