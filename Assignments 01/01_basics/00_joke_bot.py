# Constants
PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Why do programmers prefer dark mode? Because light attracts bugs!"
SORRY = "Sorry I only tell jokes"

def main():
    # Prompt the user for input
    user_input = input(PROMPT)
    
    # Check if the user input is "Joke"
    if user_input == "Joke":
        print(JOKE)  
    else:
        print(SORRY) 

if __name__ == "__main__":
    main()
