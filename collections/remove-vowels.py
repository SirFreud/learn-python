def main():
	user_input = input("Please type a list of words separated by commas: ")
	user_input = user_input.replace(" ", "").split(',')
	print(user_input)
	remove_vowels(user_input)

def remove_vowels(user_input):

	for letter in user_input:

		if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
			try:
				user_input.remove(letter)
			except ValueError:
				continue
		else:
			user_input.join(letter)
			print(user_input)
	return user_input

main()




