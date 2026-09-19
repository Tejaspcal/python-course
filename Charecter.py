worldman = input("Enter your own word kid: ")
thecharacter = input("Enter your own character kid: ")
i = 0
C = 0
while i < len(worldman):
  if (worldman[i] == thecharacter):
    C = C + 1
  i = i + 1
print("The character appears", C, "times in the word.")