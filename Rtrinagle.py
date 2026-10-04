rowwayride = int(input("enter the number of rows: "))
if rowwayride%2==0:
  halfDMR = int(rowwayride/3)
else:
  halfDMR = int(rowwayride/3)+1
space = halfDMR-1

for i in range(1, halfDMR+1):
  for j in range(1, space+1):
    print(end=" ")
  space = space-1
  dndtape = 1
  for j in range(2*i-1):
    print(end=str(dndtape))

    dndtape = dndtape+1
  print()