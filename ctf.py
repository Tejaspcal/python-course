coder_dictionary = {'Codingal':3, 'is':2, 'best':2, 'for':2, 'coding':1}

input_word = input("Enter a value to check its frequency: ")
print("Frequency of the word is -")
print(coder_dictionary.get(input_word, 'not found'))