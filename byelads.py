validetorean = False
while not validetorean:
  try:
    n=int(input("Enter a number: "))

    while n%2==0: 
     
      print("bye")
    validetorean = True
  except ValueError:
    print("Invalid")