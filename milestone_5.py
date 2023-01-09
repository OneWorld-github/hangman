#milestone_5

# Create a function that will run all the code to run the game as expected. 
# You should begin by creating a new script called milestone_5.py. 
# Copy all the codes in milestone_4.py file into the newly created milestone_5.py file.

# Step 1. Create a function called play_game that takes word_list as a parameter. 
# Inside the function, write the code for the following steps

# Step 2. Create an instance of the Hangman class. 
# Do this by calling the Hangman class and assign it to a variable called game.

# Step 3. Pass word_list and num_lives as arguments to the game object.

# Step 4. Create a while loop and set the condition to True. In the body of the loop, do the following

# 1. Check if the `num_lives` is 0. If it is, that means the game has ended and the user lost. 
# Print a message saying 'You lost!'.
# 2. Next, check if the `num_letters` is greater than 0. 
# In this case, you would want to continue the game, so you need to call the `ask_for_input` method. 
# 3. If the `num_lives` is not 0 and the `num_letters` is not greater than 0, 
# that means the user has won the game. Print a message saying 'Congratulations. You won the game!'.


import random

class Hangman:
    def __init__(self, word_list, num_lives=9):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        
    def check_guess(self):
        self.guess.lower()
        if self.guess in self.word:
            print(f"Good guess! {self.guess} is in the word")
            
            for index, letter in enumerate(self.word):
                if letter == self.guess:
                    self.word_guessed[index] = self.guess
                    self.num_letters -= 1
        
        else:
            self.num_lives -= 1
            print(f"Sorry, {self.guess} is not in the word.")
            print(f" You have {self.num_lives} lives left.")
            
            self.list_of_guesses.append(self.guess)
            
    def ask_for_input(self):
        while True:
            
            self.guess = input("Guess a letter ")
            if len(self.guess) == 1 and self.guess.isalpha() and self.guess not in self.list_of_guesses:
                print("Good Guess, it's a single character, and you've not guessed this one yet")
                self.list_of_guesses.append(self.guess)
                self.check_guess()
                break
            if len(self.guess) > 1:
                print("please guess a single character")
            if not self.guess.isalpha():
                print("please guess an alphabetic character")
            elif self.guess in self.list_of_guesses:
                print("You have already tried this letter")
            else:
                print("Try another letter ?")        
                
def play_game(word_list):
    game = Hangman(word_list)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            print("The word you have to guess: ", game.word_guessed)
            game.ask_for_input()
            
        elif game.num_lives != 0 and game.num_letters < 1:
            print("Welldone, the word was: ", )
            print('Congratulations. You won the game!, The Word Was: ', ''.join(game.word_guessed))
            break

word_list = ['blueberries', 'raspberries', 'kiwi', 'orange', 'pear']
play_game(word_list)