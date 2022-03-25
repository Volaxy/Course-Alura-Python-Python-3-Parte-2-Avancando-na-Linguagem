import random


def __main__():
    file = open("words.txt", "r")

    print("The words in the file is:")
    print(file.read())
    file.close()

    option = int(input("""Do you want add more words or play the game?
(1) - Add more words
(2) - Play the Hangman Game
-> """))

    if option == 1:
        file = open("words.txt", "a")

        finished = "n"
        while finished == "n":
            word = input("Which word do you want to add? ")
            file.write("\n" + word)

            finished = input("Finished? (Any key) To yes, (N) To no: ").lower()

        file.close()
    if option == 2:
        file = open("words.txt", "r")

        words = []
        for word in file:
            words.append(word)

        secret_word = random.choice(words)

        word = []
        for i in range(len(secret_word) - 1):
            word.append("_")

        # Player
        end_game = False
        used_letters = []
        while not end_game:
            for letter in word:
                print(letter, end="")
            print()

            kick_letter = input("Which letter do you want to kick? ")
            used_letters.append(kick_letter)

            index = 0
            for letter in secret_word:
                if kick_letter == letter:
                    word[index] = letter

                index += 1

            if word.count("_") == 0:
                end_game = True

        file.close()


if __name__ == "__main__":
    __main__()
