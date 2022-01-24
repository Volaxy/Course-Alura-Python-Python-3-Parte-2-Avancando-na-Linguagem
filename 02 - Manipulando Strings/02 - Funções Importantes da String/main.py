import hangmanGame
import divination


def chose_game():
    print("*********************************")
    print("*******Chose a game!*******")
    print("*********************************")

    print("(1) Hangman Game (2) Divination")

    game = int(input("which game? "))

    if game == 1:
        print("Playing Hangman")
        hangmanGame.play_hangman()
    elif game == 2:
        print("Playing Divination")
        divination.play_divination()


# The "__name__" is a variable when the python file is loaded, and from this variable, the code is executed
if __name__ == "__main__":
    chose_game()
