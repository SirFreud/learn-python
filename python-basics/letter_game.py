import random
import os
import sys

# Make a list of words
words = [

	'apple',
	'banana',
	'orange',
	'strawberry',
	'lemon',
	'grapefruit',
	'blueberry',
	'melon'
]

def clear():
	if os.name =='nt':
		os.system('cls')
	else:
		os.system('clear')

def draw(bad_guesses, good_guesses, secret_word):
	clear()
	print('Strikes: {} out of {}'.format(len(bad_guesses), number_of_guesses))
	print('')

	for letter in bad_guesses:
		print(letter, end=' ')
	print('\n\n')

	for letter in secret_word:
		if letter in good_guesses:
			print(letter, end='')
		else:
			print('_', end='')

	print('')

def get_guess(bad_guesses, good_guesses):
	while True:
		# Take guess
		guess = input("Guess a letter: ").lower()
		if len(guess) != 1:
			print("You can only guess 1 letter at a time")
			continue
		if guess in bad_guesses or guess in good_guesses:
			print("You've guessed that letter already!")
			continue
		if not guess.isalpha():
			print("You can only guess letters!")
			continue
		return guess
		break

def play(done):
	clear()
	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = []
	number_of_guesses = 7

	while True:
		draw(bad_guesses, good_guesses, secret_word)
		guess = get_guess(bad_guesses, good_guesses)
		if guess in secret_word:
			good_guesses.append(guess)
			found = True
			for letter in secret_word:
				if letter not in good_guesses:
					found = False
			if found:
				print("You win! The secret word was: {}".format(secret_word))
				done = True
		else:
			bad_guesses.append(guess)
			if len(bad_guesses) == number_of_guesses:
				print("You lost! The secret word was: {}".format(secret_word))
				done = True

		if done:
			play_again = input("Would you like to play again? Y/N").lower()
			if play_again != 'n':
				return play(done=False)
			else:
				sys.exit()

def welcome():
	start = input("Press enter to begin or Q to quit: ")
	if start == 'q':
		print("Bye! \n")
		sys.exit()
	else:
		return True
print("Welcome to Letter Game!")
done = False

while True:
	clear()
	welcome()
	play(done)
