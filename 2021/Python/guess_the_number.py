import random

if __name__ == "__main__":
    correct_number = random.randint(1, 100)
    is_win = False
    x = int(input("Please select number of turns you want to guess\n"))
    for i in range(x):
        guess_number = int(input("Guess the number between 1-100\n"))
        if guess_number == correct_number:
            is_win = True
            break
        elif guess_number > correct_number:
            print("You have guessed higher. Lower your expectations. Turn remains {}.\n".format(x - i - 1))
        elif guess_number < correct_number:
            print("You have guessed Lower. Higher your expectations. Turn remains {}.\n".format(x - i - 1))
    if is_win:
        print("Winner, Winner. Chicken Dinner!!!\n")
    else:
        print("You loose!!The number was {}.".format(correct_number))
