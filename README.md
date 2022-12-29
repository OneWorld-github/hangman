# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The Hangman Class is defined with the following attributes:-

Word is the secret word picked randomly from the list of words.  
Word List is the list of words.  
Word guessed is a list of letters initialised as underscores for each item in the list.
num_letters is an integer of the number of letters remaining to be guessed.
num_lives is the number of lives you have left.  This decrements each time the player guesses a character incorrectly.
Also a list of guesses is stored, so you know what you have tried already.

## Methods
<b>check_guess</b> method checks if the character guessed is in the word
if it is then it puts the correctly guessed letter into its correct place in the word guessed, and it decrements the number of letters left to guess by 1.

If the guess is incorrect it reduces the remaining number of lives by 1.
and appends the guessed letter to the list of guesses, so you can see what guesses have been guessed.


<b>ask_for_input</b> method asks the user for input, converts the input to a lowercase string.It checks 
if the input is 1 letter.
if the letter has already been tried
if it is 1 letter and hasn't been tried yet we append to our list of tried letters.
else we run the check guess
