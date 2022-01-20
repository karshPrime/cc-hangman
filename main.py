#!/usr/bin/env python

from random import choice

words = ["lemon", "textas", "yellow", "fidget", "staple", "paper", "keyboard"]
random_word = choice(words)

# would be called for correct input
def correct_answer(score):
    print("Congratulations! On to the next letter!")
    print(f"Your score is {score}")

# would be called for wrong input. would also output hangman figure
def wrong_answer(score, wrong_count):
    if wrong_count == 5:
        print("Game over\nyou lost")
        return 0
    else:
        hangman = [r"   O   " ,r"   |   " ,r"-------" ,r"   |   " ,r"   /\   "]
        print("\n".join(hangman[0:wrong_count]))
        print("Onto the next letter.")
        return 1

# gets inptut from user. doesn't accept non-one-digit inputs or non-alphabetical inputs
def get_input(score, message="Guess: "):
    guess = (input(message))
    if (len(guess) == 1) and (ord(guess.lower()) in range(97, 123)):
        return guess
    else:
        get_input(score, "Invalid input, please try again: ")

# will calculate player score, and remaining chances
def chances_left(on_letter, score, wrong_count, result):
    guess = get_input(score)
    if guess.lower() == random_word[on_letter]:
        on_letter += 1
        score += 1
        correct_answer(score)
    else:
        score -= 1
        wrong_count += 1
        result = wrong_answer(score, wrong_count)
    
    recursion_function(on_letter, score, wrong_count, result)

# will recall chances_left if game isn't over
def recursion_function(on_letter, score, wrong_count, result):
    if (on_letter) == len(random_word):
        print("you won!")
    elif result == 1:
        chances_left(on_letter, score, wrong_count, result)

def main():
    print("Welcome to Hangman!")
    print(f"Please guess the first letter of your word, which has {len(random_word)} characters.")
    print(random_word)
    result, on_letter, score, wrong_count = 1, 0, 0, 0
    chances_left(on_letter, score, wrong_count, result)

main()
