A = int(input("Enter the Amount you have: "))

note_1 = A//100
note_2 = (A%100)//50
note_3 = ((A%100)%50)//10


print("notes of 100 dollar", note_1)
print("notes of 50 dollar", note_2)
print("notes of 10 dollar", note_3)