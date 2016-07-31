import random

def game():
	# generate a random number between 1-10
	secret_num = random.randint(1, 10)
	guess_count = 0

	while True:
		# get a number guess from player
		try:
			guess = int(input("Guess a number between 1 and 10: "))
		except ValueError:
			print("That's not a number, try again!")
			continue
		if guess > 10 or guess < 1:
			print("You didn't pick a number between 1 and 10")
			continue

		# compare to secret number
		if guess == secret_num:
			print("\nCongrats, you guessed the number correctly!")
			break

		if guess <= secret_num:
			print("You guessed lower than the secret number, try a higher number!")
			guess_count += 1

		if guess >= secret_num:
			print("You guessed a higher number than the secret, go lower!")
			guess_count += 1

		# Check guess count
		if guess_count >= 5:
			print("\nYou hit your 5 guess max....you lose")
			break
game()