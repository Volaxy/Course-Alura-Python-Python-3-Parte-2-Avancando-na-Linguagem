"""
It is always important to give feedback to the user when he takes some action on the system.
In the case of the hangman, when the player misses a letter, we want to indicate this,
along with how many attempts are left.
In other words, we want to show the player how many rounds he can play before being hanged.

What code could we write to give this feedback to the player?
"""


def play_hangman():
    print("*********************************")
    print("***Welcome to the game of Hangman!***")
    print("*********************************")

    secret_word = "banana".lower()
    correct_letters = ["_", "_", "_", "_", "_", "_"]
    print(correct_letters)

    hanged = False
    win = False
    errors = 0
    while not hanged and not win:
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
