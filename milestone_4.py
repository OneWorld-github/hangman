# %%
# Milestone 4
import random

#Task 1
class Hangman:
    def __init__(self, word_list):
        self.word = random.choice(word_list)
        self.word_list = word_list
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.num_lives = 9 # like a cat.
        self.list_of_guesses = []
        
    #Task2
    # In this task, you will create a method that will ask the user to guess a letter and another method that will check if the guess is in the word.
    # Remember that a method is a function that is defined inside a class.
    # Let's create the check_guess method.
    # Step 1: Define a method called check_guess. Pass the guess to the method as a parameter. In the body of the method, write the code for the following steps:
    # Convert the guessed letter to lower case
    # Create an if statement that checks if the guess is in the word
    # In the body of the if statement, print a message saying "Good guess! {guess} is in the word."
    # You will continue with the logic of the check_guess method in the next task. For now, let's create the ask_for_input method.

    def check_guess(self):
        self.guess.lower()
        if self.guess in self.word:
            print(f"Good guess! {self.guess} is in the word")
            # Task 3
            # Return to your check_guess method and extend it to replace the underscore(s) in the word_guessed with the letter guesssed by the user.
            # In the if block of your check_guess method, after your print statement, do the following:
            # Create a for-loop that will loop through each letter in the word.
            # Within the for-loop, do the following:
            # Create an if statement that checks if the letter is equal to the guess.
            # In the if block, replace the corresponding "_" in the word_guessed with the guess. HINT: You can index the word_guessed at the position of the letter and assign it to the letter.
            # Outside the for-loop, reduce the variable num_letters by 1.
            
            for index, letter in enumerate(self.word_guessed):
                if letter == self.guess:
                    self.word_guessed[index] = self.guess
            self.num_letters -= 1
        
        # Task 4
        # Define what happens if the guess is not in the word you are trying to guess.
        # Step 1. In the check_guess method, Create an else statement.
        # Step 2: Within the else block: Reduce `num_lives' by 1.
        # print a message saying "Sorry, {letter} is not in the word."
        # print another message saying "You have {num_lives} lives left."
        # Step 3. Lastly, append the guess to the list_of_guesses. Ensure you do this outside the else block so that the letter can be appended to the list_of_guesses in both conditions.
        
        else:
            self.num_lives -= 1
            print(f"Sorry, {self.guess} is not in the word.")
            print(f" You have {self.num_lives} left.")
            self.list_of_guesses.append(self.guess)
            
            
    # Task 2
    # Step 1. define a method called ask_for_input. In the body of the method, do the following:
    # Create a while loop and set the condition to True.
    # Ask the user to guess a letter and assign this to a variable called guess.
    # Create an if statement that runs if the guess is NOT a single alphabetical character.
    # In the body of the if statement, print a message saying "Invalid letter. Please, enter a single alphabetical character."
    # Create an elif statement that checks if the guess is already in the list_of_guesses.
    # In the body of the elif statement, print a message saying "You already tried that letter!".
    # If the guess is a single alphabetical character and it's not already in the list_of_guesses:
    # Create an else block and call the check_guess method. Remember to pass the guess as an argument to this method.
    # Add the guess to the `list_of_guesses.
    # Step 2. Call the ask_for_input method to test your code.
    # That was a lot! Keep going, you are almost there.
    def ask_for_input(self):
        not_correct = True
        while not_correct:
            self.guess = input("Guess a letter")
            if len(self.guess) == 1 and self.guess.isalpha:
                print("Good Guess")
                not_correct = False
            elif self.guess in self.list_of_guesses:
                print("You have already tried this letter")                
            if len(self.guess) == 1 and self.guess.isalpha and self.guess not in self.list_of_guesses:
                self.list_of_guesses.append(self.guess)
            else:
                self.check_guess(self.guess)
#Step2
new_game = Hangman(word='word', word_list=['a', 'word', 'or', 'two'])
new_game.ask_for_input()



# %%
