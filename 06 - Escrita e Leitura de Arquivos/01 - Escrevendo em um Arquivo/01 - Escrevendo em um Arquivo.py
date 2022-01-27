def write_in_file():
    """
    To open a file, the Python have the function built-in "open()". She receives two parameters: The first is the name
    of the file to be open, and the second is the mode witch we're working with this file, if we want "read" or "write".
    The mode is passed through by string: "w" for writing and "r" to reading.
    """
    file = open("words.txt", "w")

    # Remember that "w" overwrites the file, if it exists. If we just want to add content to the file, we use "a".
    # Now that we have the file, how do we write to it? Just call the write function in the file, passing to it what we
    # want to write in the file:
    file.write("banana")
    file.write("apple")

    # To close a file, use the function "close()"
    # It's good practice closing the file after using it for writing or reading, so other programs or processes can
    # have access to the file, and it doesn't just get stuck in our Python script.
    file.close()

    # To represent a new line in code, we add the \n to the end of what we want to write, this time using the "a",
    # of append:
    file = open("words.txt", "a")

    file.write("\nStrawberry")
    file.write("\nwatermelon")

    # If the second parameter not passed in the function, the default access modifier is the "r" (read)


if __name__ == "__main__":
    write_in_file()
