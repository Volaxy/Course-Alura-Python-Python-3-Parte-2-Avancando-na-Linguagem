def play_hangman():
    print("*********************************")
    print("***Welcome to the game of Hangman!***")
    print("*********************************")

    secret_word = "banana"
    correct_letters = ["_", "_", "_", "_", "_", "_"]
    print(correct_letters)

    hanged = False
    win = False
    while not hanged and not win:
        print("Playing...")

        kick = input("Write a letter: ")

        kick = kick.strip()

        index = 0
        for letter in secret_word:
            if kick.lower() == letter:
                print("Letter {} found in the index {}".format(letter, index))
                correct_letters[index] = kick

            index += 1

        print(correct_letters)

    print("Game Over")


if __name__ == "__main__":
    play_hangman()
