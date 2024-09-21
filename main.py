# main.py

def main():
    # Define the relative path to the book file
    path_to_file = 'books/frankenstein.txt'
    
    # Open and read the file
    with open(path_to_file, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    
    # Print the contents of the file to the console
    print(file_contents)

# Call the main function to run the program
if __name__ == "__main__":
    main()

# main.py

def count_words(text):
    """Returns the number of words in the given text."""
    words = text.split()  # Split the text into words based on whitespace
    return len(words)     # Return the total number of words

def main():
    # Define the relative path to the book file
    path_to_file = 'books/frankenstein.txt'
    
    # Open and read the file
    with open(path_to_file, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    
    # Print the contents of the file to the console (optional)
    # print(file_contents)
    
    # Count the words in the book
    word_count = count_words(file_contents)
    
    # Print the word count
    print(f"The book contains {word_count} words.")

# Call the main function to run the program
if __name__ == "__main__":
    main()

# main.py

def count_words(text):
    """Returns the number of words in the given text."""
    words = text.split()  # Split the text into words based on whitespace
    return len(words)     # Return the total number of words

def count_characters(text):
    """Returns a dictionary with the count of each character in the given text."""
    char_count = {}  # Dictionary to store character counts
    text = text.lower()  # Convert the entire text to lowercase

    # Iterate through each character in the text
    for char in text:
        if char.isalpha():  # Count only alphabetic characters (ignores punctuation, spaces, etc.)
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count  # Return the dictionary of character counts

def main():
    # Define the relative path to the book file
    path_to_file = 'books/frankenstein.txt'
    
    # Open and read the file
    with open(path_to_file, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    
    # Count the words in the book
    word_count = count_words(file_contents)
    
    # Count the characters in the book
    char_count = count_characters(file_contents)
    
    # Print the word count
    print(f"The book contains {word_count} words.")
    
    # Print the character count dictionary
    print("Character frequencies:")
    print(char_count)

# Call the main function to run the program
if __name__ == "__main__":
    main()

# main.py

def count_words(text):
    """Returns the number of words in the given text."""
    words = text.split()  # Split the text into words based on whitespace
    return len(words)     # Return the total number of words

def count_characters(text):
    """Returns a dictionary with the count of each character in the given text."""
    char_count = {}  # Dictionary to store character counts
    text = text.lower()  # Convert the entire text to lowercase

    # Iterate through each character in the text
    for char in text:
        if char.isalpha():  # Count only alphabetic characters (ignores punctuation, spaces, etc.)
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count  # Return the dictionary of character counts

def print_report(file_name, word_count, char_count):
    """Prints a report of word and character counts."""
    # Print the report header
    print(f"--- Begin report of {file_name} ---")
    
    # Print the word count
    print(f"{word_count} words found in the document")
    print()

    # Sort the character counts alphabetically and print them
    for char in sorted(char_count.keys()):
        print(f"The '{char}' character was found {char_count[char]} times")

    # Print the report footer
    print("--- End report ---")

def main():
    # Define the relative path to the book file
    path_to_file = 'books/frankenstein.txt'
    
    # Open and read the file
    with open(path_to_file, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    
    # Count the words in the book
    word_count = count_words(file_contents)
    
    # Count the characters in the book
    char_count = count_characters(file_contents)
    
    # Print the report
    print_report(path_to_file, word_count, char_count)

# Call the main function to run the program
if __name__ == "__main__":
    main()
