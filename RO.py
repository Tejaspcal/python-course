ultimate_number = int(input("Enter your ultimate number: "))

add = 0
while ultimate_number > 0:
    add = add + 1
    ultimate_number = int(ultimate_number / 10)

print("The total digits of the ultimate number that you have entered is:", add)