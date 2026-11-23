western_code = {'USA': '+1', 'Canada': '+5', 'UK': '+44'}

print("Contry code for Canada -")
print(western_code.get('Canada', 'not found'))

print("Contry code for Russia -")
print(western_code.get('Russia', 'not found'))