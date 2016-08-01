def main():
	user_input = input("Please type a list of words separated by commas: ")
	user_input = user_input.replace(" ", "").split(',')
	print(user_input)
	remove_vowels(user_input)

def remove_vowels(list_of_user_input):

	for word in list_of_user_input:
		for letter in list_of_user_input[word]:
			if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
				try:
					list_of_user_input.remove(letter)
				except ValueError:
					continue
			else:
				list_of_user_input.join(letter)
				print(list_of_user_input)
	return list_of_user_input

main()