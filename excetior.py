try:
    dashcam = int(input("Enter a value of the number: "))
    print("The value of the number is", dashcam)
except ValueError as ex:
    print("The value of the number is not an integer:", ex)