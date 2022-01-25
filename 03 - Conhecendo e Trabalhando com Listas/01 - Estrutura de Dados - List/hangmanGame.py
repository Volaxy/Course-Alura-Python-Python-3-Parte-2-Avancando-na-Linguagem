def play_hangman():
    print("*********************************")
    print("***Welcome to the game of Hangman!***")
    print("*********************************")

    secret_word = "banana"

    hanged = False
    win = False
    while not hanged and not win:
        print("Playing...")

        kick = input("Write a letter: ")

        kick = kick.strip()

        index = 0
        for letter in secret_word:
            if kick.lower() == letter:
                print(kick)
                print("Letter {} found in the index {}".format(letter, index))

            index += 1

    print("Game Over")


if __name__ == "__main__":
    play_hangman()
