#Task 1 Iteratively check if theinput is a valid guess
#Write code that will continuously ask the user for a letter and validate it.
# Create a new script called milestone_3.py. 
# This file will contain the code for this milestone.

# Step 1. Create a while loop and set the condition to True. 
# Setting the condition to True ensures that the code run continuously. 
# In the body of the loop, write the code required for the following steps.

# Step 2: Ask the user to guess a letter and assign this to a variable called guess.
# Step 3. Check that the guess is a single, alphabetical character.
# Step 4. If the guess passes the checks, break out of the loop.

# Step 5: If the guess does not pass the checks, 
# then print a message saying "Invalid letter. 
# Please, enter a single alphabetical character."
# %%
# not_correct = True
# while not_correct:
#     guess = input("Guess a letter")
#     if len(guess) == 1 and guess.isalpha:
#         print("Good Guess")
#         not_correct = False
#     else:
#         print("Invalid letter, please enter a single alphabetical character")
    


# %%
# Task 2
# Check whether the letter guessed by the user is in the secret 
# word that was randomly chosen by the computer. For example, 
# if the user guesses the letter "a" and the secret word is "apple", 
# then your code should check if "a" is in "apple".

# Step 1. Create an if statement that checks if the guess is in the word.

# Step 2. In the body of the if statement, 
# print a message saying "Good guess! {guess} is in the word.". 
# Obviously, format the string to show the actual guess 
# instead of {guess}.

# Step 3. Create an else block that prints a message saying "Sorry, 
# {guess} is not in the word. Try again." 
# This block of code will run if the guess is not in the word.

# if guess in secret_word:
#     print(f"Good guess! {guess} is in the word")
# else:
#     print(f"Sorry, {guess} is not in the word. Try again.")

    
# %%
# Task 3
#Good job so far! But your code probably doesn't look great. 
# It's hard to tell which lines do what.
# Create 2 functions, check_guess and ask_for_input functions 
# which contain the code for those two things.

# The check_guess function will take the guessed letter as an argument 
# and check if the letter is in the word.

# Step 1: Define a function called check_guess. pass in the guess as 
# a parameter for the function. Write the code for the following steps 
# in the body of this function.

# Step 2: Convert the guess into lower case.

# Step 3. Move the code that you wrote to check if the guess is in 
# the word into this function block.

# The ask_for_input.
# Step 1. Define a function called ask_for_input
# Step 2. Move the code that you wrote in the Iteratively check if the 
# input is a valid guess task into this function block.
# Step 3. Outside the while loop, but within this function, call the 
# check_guess function to check if the guess is in the word. Don't forget 
# to pass in the guess as an argument to the method.

# Step 4. Outside the function, call the ask_for_input function to test 
# your code.

# %%

def check_guess(guess, word):
    guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
    

def ask_for_input(word):
    while True:
        guess = input("Guess a letter")
        if len(guess) == 1 and guess.isalpha():
            print("Good Guess")
            break
        else:
            print("Invalid letter, please enter a single alphabetical character")
    check_guess(guess, word)

ask_for_input('apple')

