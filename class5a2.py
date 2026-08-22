real_cost = float(input("Enter the real cost of the item: "))
sale_amount = float(input("Enter the sale amount: "))

if (sale_amount>real_cost):
    amount_saved = sale_amount - real_cost
    print("You saved: $", amount_saved)
else:
    print("sorry but you have not made any profit")