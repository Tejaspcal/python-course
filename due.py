totaltcost = float(input("Enter the total cost: "))
paidcost = float(input("Enter the amount that you paid: "))

def func(totaltcost, paidcost):
    return(totaltcost - paidcost)

additional_cost = func(totaltcost, paidcost)
print("Visual will get about", additional_cost, "back.")