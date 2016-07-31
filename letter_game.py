import random
import os
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

number_of_guesses = 7
while True:
	start = input("Press Enter to start the game or type Q to quit: ")
	if start.lower() == 'q':
		break

	# Pick a random word - choice method picks a random item out of an iterable
	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = []

	while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):





		if guess.lower() in secret_word.lower():
			good_guesses.append(guess)
			x = len(list(secret_word))
			y = len(good_guesses)
			if len(good_guesses) == len(list(secret_word)):
				print("You win! The word was {}".format(secret_word))
				print("")
				break
		if guess not in secret_word:
			bad_guesses.append(guess)


	# Print win or loss
	else:
		print("You didn't guess it! My secret word was {}".format(secret_word))


