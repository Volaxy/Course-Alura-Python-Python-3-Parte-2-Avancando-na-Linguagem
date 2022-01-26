"""
We saw in this chapter that the "hit" and "hanged" variables were used to control the loop's output.
As long as they are not true, the code inside the loop will be executed.
In order for the loop to end, we create assignments for these variables.

However, this is not the only way to get out of a loop.
We can also use the break keyword which, when executed, will terminate the loop at that point.
How can we change our force code to use break and exit while?
"""


def play_hangman():
    print("*********************************")
    print("***Welcome to the game of Hangman!***")
    print("*********************************")

    secret_word = "banana".lower()
    correct_letters = ["_", "_", "_", "_", "_", "_"]
    print(correct_letters)

    errors = 0
    while True:
        print("\n{} chances remaining...".format(abs(errors - 6)))
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

        if errors == 6:
            break
        if "_" not in correct_letters:
            break

        print(correct_letters)

    if win:
        print("You win! :D")
    else:
        print("You lose! :(")

    print("Game Over")


if __name__ == "__main__":
    play_hangman()
