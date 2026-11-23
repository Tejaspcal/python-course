test_dict = {'sms' : 1, 'email' : 2, 'push' : 3}

print("Dictionary keys:" + str(test_dict))

A = 2

res = 0

for key in test_dict:
    if test_dict[key] == A:
        res = res + 1

print("Frequency of A is :" + str(res))