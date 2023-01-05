#milestone_2.py
#Task 1
# %%
word_list = ['blueberries', 'raspberries', 'kiwi', 'orange', 'pear']
print(word_list)

# %%
#Task 2
import random
word = random.choice(word_list)
print(word)
# %%
guess = input("Please enter a single letter")
if len(guess) == 1 and guess.isalpha():
    print("Good Guess")
else:
    print("oops that is not a valid input")

