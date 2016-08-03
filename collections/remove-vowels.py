def main():
	user_input = input("Please type a list of words separated by commas: ")
	user_input = user_input.replace(" ", "").split(',')
	remove_vowels(user_input)

def remove_vowels(list_of_user_input):

	no_vowels = []

	for word in list_of_user_input:
		for letter in list_of_user_input[word]:
			if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
				list_of_user_input.remove(letter)
			else:
				continue
		no_vowels.append(word)
	return no_vowels

main()