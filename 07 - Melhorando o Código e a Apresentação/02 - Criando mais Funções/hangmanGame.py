import random


def play_hangman():
    print_welcome_game()

    secret_word = chose_secret_word()

    correct_letters = ["_" for _ in secret_word]

    print(correct_letters)

    hanged = False
    win = False
    errors = 0
    while not hanged and not win:
        print("Playing...")

        kick = input("Write a letter: ")
        kick = kick.strip().lower()

        if kick in secret_word:
            replace_with_kick(kick, secret_word, correct_letters)
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


# Print welcome messages in the game begin
def print_welcome_game():
    print("*************************************")
    print("***Welcome to the game of Hangman!***")
    print("*************************************")


# Chose a secret word of the file "words.txt"
def chose_secret_word():
    file = open("words.txt", "r")
    words = [word.strip() for word in file]

    file.close()

    sorted_word = random.randrange(0, len(words))

    secret_word = words[sorted_word].lower()

    return secret_word


# Replace the "correct_letters" with the letter give by the user
def replace_with_kick(kick, secret_word, correct_letters):
    index = 0
    for letter in secret_word:
        if kick == letter:
            print("Letter {} found in the index {}".format(letter, index))
            correct_letters[index] = kick

        index += 1


if __name__ == "__main__":
    play_hangman()
