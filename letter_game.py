import random

# Make a list of words
words = [

	'Apple',
	'Banana',
	'Orange',
	'Strawberry',
	'Lemon',
	'Grapefruit',
	'Blueberry',
	'Melon'
]

number_of_guesses = 7

while True:
	start = input("Press Enter to start the game or type Q to quit: ")
	if start.lower() == 'q':
		break

	# Pick a random word - choice method picks a random item out of an iterable
	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = []

	while len(bad_guesses) < number_of_guesses and len(good_guesses) != len(list(secret_word)):
		# Draw spaces, guessed letters and strikes
		for letter in secret_word.lower():
			if letter in good_guesses:
				print(letter, end='')
			else:
				print('_', end='')
		print('')
		print('Strikes: {} out of {}'.format(len(bad_guesses), number_of_guesses))
		print('')

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


		if guess.lower() in secret_word.lower():
			good_guesses.append(guess)
			if len(good_guesses) == len(list(secret_word)):
				print("You win! The word was {}".format(secret_word))
				print("")
				break
		if guess not in secret_word:
			bad_guesses.append(guess)


	# Print win or loss
	else:
		print("You didn't guess it! My secret word was {}".format(secret_word))


