decimalnumber = float(input("Enter the your decimal number for a binary number: "))

decimalpart = bin(int(decimalnumber))

binarynumber = decimalpart[2:]

print(f"The prefix of the decimal number is {decimalnumber}")
print(f"The clean binary number is {binarynumber}")