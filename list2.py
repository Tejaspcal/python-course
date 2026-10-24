def match_man(words):
    crt = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            crt += 1
            lst.append(word)


    print("Number of words that match the criteria:\n", lst)

    return crt
countermachinery = match_man(['abc', 'xyz', 'aba', '1221'])
print("Total count of matching words:", countermachinery)