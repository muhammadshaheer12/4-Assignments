def main():
    # Define the beginning of the sentence
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

    # Prompt the user for input
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Construct the full sentence
    sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"

    # Print the result
    print(sentence)

if __name__ == "__main__":
    main()
