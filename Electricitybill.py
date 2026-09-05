Unitbars = int(input("Enter the number of unit bars consumed: "))
if (Unitbars <= 50):
    bill = Unitbars * 3.50
    charge=25

elif (Unitbars <= 100):
    bill = 130 + (Unitbars - 50) * 4.50
    print(f"Your electricity bill is: {bill}")
elif (Unitbars <=200):
    bill = 50 * 3.50 + 50 * 4.50 + (Unitbars - 100) * 6.50
    print(f"Your electricity bill is: {bill}")
else:
    bill = 50 * 3.50 + 50 * 4.50 + 100 * 6.50 + (Unitbars - 200) * 8.50
    print(f"Your electricity bill is: {bill}")