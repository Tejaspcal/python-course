import random
play_boy = True
numberzone = str(random.randint(1, 12))
print("I will start generating the number between 1 to 12")
print("The game will end when you guess the correct number")

while play_boy:
        guess = input("Enter your guess:\n")
        if numberzone == guess:
                print("You will win the game")
                print("your number is",numberzone)
                break
        else:
            print("The number is not correct")