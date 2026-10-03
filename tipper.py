def Tipper_calculation(bill_amount, tip_percentage):
    tip = bill_amount * (1 + 0.01*tip_percentage)
    total_amount = round(tip,2)
    print("The total amount to be paid is: ", total_amount)

Tipper_calculation(1000, 190)