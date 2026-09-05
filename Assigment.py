bannanacon = input("what is your medical condition: (Y/N)").strip().upper()

if bannanacon == "Y":
    print("Please consult a doctor.")
else:
  go = int(input("Enter your atendence: "))
  if go >= 75:
    print("Your allowed to go to your classes.")
  else:
    print("You have to go home.")