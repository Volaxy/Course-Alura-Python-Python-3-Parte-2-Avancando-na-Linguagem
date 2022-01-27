import random


def play_hangman():
    print("*********************************")
    print("***Welcome to the game of Hangman!***")
    print("*********************************")

    file = open("words.txt", "r")
    words = [word.strip() for word in file]

    file.close()

    # The "randrange()" chose a number in the interval of the arguments
    sorted_word = random.randrange(0, len(words))

    secret_word = words[sorted_word].lower()
    correct_letters = ["_" for letter in secret_word]

    print(correct_letters)

    hanged = False
    win = False
    errors = 0
    while not hanged and not win:
        print("Playing...")

        kick = input("Write a letter: ")
        kick = kick.strip().lower()

        if kick in secret_word:
            index = 0
            for letter in secret_word:
                if kick == letter:
                    print("Letter {} found in the index {}".format(letter, index))
                    correct_letters[index] = kick

                index += 1
        else:
            errors += 1

        hanged = errors == 6
        win = "_" not in correct_letters

        print(correct_letters)

    if win:
        print("You win! :D")
    else:
        print("You lose! :(")

    print("Game Over")


if __name__ == "__main__":
    play_hangman()
