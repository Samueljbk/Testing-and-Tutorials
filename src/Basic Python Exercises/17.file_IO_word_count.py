# Write a Python program to count the frequency of words in a file.


# Function to count the frequency of words in a file
def count_word_frequency(file_name):
    with open(file_name, "r") as file:
        # Read the content of the file
        content = file.read().lower()

        # Split the content into words
        words = content.split()

        # Create an empty dictionary to store the word frequency
        word_frequency = {}

        # Loop through each word and update its count in the dictionary
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        return word_frequency


# Main function to run the program
if __name__ == "__main__":
    file_name = "input_file.txt"
    word_frequency = count_word_frequency(file_name)

    print("Frequency of words in the file:")
    for word, count in word_frequency.items():
        print(f"{word}: {count}")
