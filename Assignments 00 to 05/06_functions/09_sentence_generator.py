def make_sentence(word, part_of_speech):
    # Check the part_of_speech and print the appropriate sentence
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")

def main():
    # Prompt the user for the word and the part of speech
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    
    # Call the make_sentence function with the user's input
    make_sentence(word, part_of_speech)

if __name__ == "__main__":
    main() 
