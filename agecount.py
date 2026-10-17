try:
    age = int(input("Enter the age:"))
    if(age < 0 or age > 110):
        raise ValueError
    else:
        print("the age is correct")
        if(age % 2 == 0):
            print("even")
        else:
            print("odd")

except ValueError:
    print("The age is not correct")
