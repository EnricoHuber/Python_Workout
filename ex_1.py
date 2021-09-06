import random


def guessing_game():
    guessed = False
    num = random.randint(0, 100)
    while not guessed:
        try:
            attempt = int(input("Try to guess the number! Type an integer -------> "))
        except:
            print("Wrong input, try again. Type an integer -------> ")
        if attempt == num:
            print(f"Yeah you got it! The number was {num}. Congratulations!\n")
            guessed = True
        elif attempt < num:
            print(f"{attempt} is too low, try again!\n")
        elif attempt > num:
            print(f"{attempt} is too high, try again!\n")


guessing_game()

print('Provaaaaaaaaaaa')