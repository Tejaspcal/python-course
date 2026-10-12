try:
    ninefine1, ninefine2 = 10, 0
    result = ninefine1 / ninefine2
    print("The result is:", result)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")

except syntaxError:
    print("comma is missing in the code")

except:
    print("An unexpected error occurred.")

else:
    print("The division was successful.")

finally:
    print("Execution completed.")