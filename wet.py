wether = (1,0,1,0,1,0,1)
sun = 0
rain = 0
for i in wether:
    if i == 1:
        sun += 1
    else:
        rain += 1
if sun > rain:
        print("The weather is sunny.")
else:
        print("The weather is rainy.")