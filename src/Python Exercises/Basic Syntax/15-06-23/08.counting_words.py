# Create a program that takes a string as user input and counts the number of words in the string.
# Print the word count.


def count_words(input_string):
    words = input_string.split()
    word_count = len(words)
    return word_count


user_input = input("Enter a string: ")
word_count = count_words(user_input)

print("Word count:", word_count)
