def read_a_file():
    # To read all the file, we're using the function "read()"
    file = open("words.txt", "r")

    print(file.read())

    """
    The file is like a stream of lines, which starts at the beginning of the file, as if it were the pointer.
    It goes down and reading the file, after reading everything, it is positioned at the end of the file, so when we
    call the read() function again, there is no more content, as it has all been read.

    That is, to read the file again, we must close and open it again.
    """
    file.close()

    file = open("words.txt", "r")
    for line in file:
        print(line)

    file.close()

    file = open("words.txt", "r")
    # To read a single line from the file, we use "readLine()"
    line = file.readline().strip()
    print(line)

    file.close()


if __name__ == "__main__":
    read_a_file()
