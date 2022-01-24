# The "def" creates a function with a code inside
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

        index = 0
        for letter in secret_word:
            if kick == letter:
                print(kick)
                print("Letter {} found in the index {}".format(letter, index))

            index += 1

    print("Game Over")


# The "__name__" is a variable when the python file is loaded, and from this variable, the code is executed
if __name__ == "__main__":
    play_hangman()
