# Write a Python program to write a list of words to a file,
# and then read the file and print its contents.


def read_from_file():
    with open("example.txt", "r") as file:
        print(file.read())


def write_to_file():
    user_input = input("Enter something to write to a file: ")
    with open("example.txt", "w") as file:
        file.write(user_input)


read_from_file()
