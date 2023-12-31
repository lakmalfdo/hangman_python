import random

# List of words for the Hangman game
word_list = ["elephant", "lion", "tiger", "giraffe", "zebra", "kangaroo", "penguin", "dolphin", "rhinoceros", "octopus", "cheetah", "koala", "hedgehog", "crocodile", "seagull", "panda", "otter", "polarbear", "platypus", "chimpanzee"]

# List of  hangman stage in ASCII art
hangman_stages = [
"""
________    
|    |    
|         
|         
|         
|         
=========
""",
"""
________    
|    |    
|    O    
|         
|         
|         
=========
""",
"""
________    
|    |    
|    O    
|    |    
|         
|         
=========
""",
"""
________    
|    |    
|    O    
|   /|    
|         
|         
=========
""",
"""
________    
|    |    
|    O    
|   /|\\  
|         
|         
=========
""",
"""
________    
|    |    
|    O    
|   /|\\  
|   /     
|         
=========
""",
"""
________    
|    |    
|    O    
|   /|\\  
|   / \\  
|         
=========
"""]

# Function to display the hangman stage in ASCII art
def display_hangman_stage():
    print(hangman_stages[attempts])

# Function to get the current answer
def get_answer():
    answer = ""
    for letter in word:
        if letter in guessed_letters:
            answer += letter
        else:
            answer += "_"
    return answer

# Function to display the current answer
def display_answer():
    print(get_answer())

# Maximum number of incorrect guesses allowed
max_attempts = 6

# Select a random word from the list
word = random.choice(word_list)

# Create a list to store the guessed letters
guessed_letters = []

attempts = 0

def main():
    # Display Hangman game name in ASCII art
    print("  _    _")
    print(" | |  | |")
    print(" | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __")
    print(" |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\")
    print(" | |  | | (_| | | | | (_| | | | | | | (_| | | | |")
    print(" |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|")
    print("                      __/ /")
    print("                     |___/")
    print()
    print("Guess the Animal")

    # Main loop: Handles the core gameplay until game over or player quits.
    while True:
        display_hangman_stage()
        display_answer()

        # Game loop: Iterates through game stages until game is over.
        while True:
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You've already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess not in word:
                attempts += 1

            display_hangman_stage()
            display_answer()

            if get_answer() == word:
                print("Congratulations, you've won!")
                break

            if attempts >= max_attempts:
                print("Game Over. The word was:", word)
                break

        # Select play again loop: Allows player to choose whether to play the game again.
        while True:
            play_again = input("Do you want to play again? (y/n): ").strip().lower()

            if play_again in ("y", "yes"):
                # Select a new random word from the list
                word = random.choice(word_list)
                # Clear guessed letters from previous game
                guessed_letters.clear()
                attempts = 0
                break
            elif play_again in ("n", "no"):
                print("Thank you for playing Hangman. Goodbye!")
                exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
                continue

if __name__ == '__main__':
    main()