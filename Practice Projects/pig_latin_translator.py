"""Translates a sentence into Pig Latin."""

def main():
    """Main function that runs the translator."""

    # Vowels list
    vowels = ('a', 'e', 'i', 'o', 'u')

    # While loop that keeps the program running
    while True:
        # This is where the final translated sentence will be stored
        final_string = ""

        # Get the input from the user for sentence that needs to be translated
        get_input = input("Enter a sentence: ")

        # Split the input into a list of words | "Hello my name is Bob" -> ["Hello", "my", "name", "is", "Bob"]
        split_input = get_input.split()

        # Enumerate the list of words and modify them one by one
        for i, word in enumerate(split_input):
            # Convert the word to lowercase
            word = word.lower()
            # Check if the word is a vowel, if it is then add yay to the end. If not, then add the first letter of the word to the end and add ay to the end
            if word[0] in vowels:
                word += "yay"
            else:
                word = word[1:] + word[0] + "ay"
            # Add the word to the final string
            final_string = final_string + word + " "
        # When all words have been translated, print the final string
        print(final_string)

        # Ask the user if they want to continue translating
        print("Do you want to continue translating?")
        print("Enter 'yes' or 'no'")
        answer = input()
        if answer.lower() == "no":
            break

# Run the program if not ran as a module
if __name__ == "__main__":
    main()
