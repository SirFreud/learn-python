import random
num_of_guess = 0
try:
	my_num = int(input("Enter a number that the computer can guess between 1 and 10: "))
except ValueError:
	print("Sorry, {} isn't a number!".format(my_num))

def binary_search(mid):

	if mid == my_num:
		print("{} is right, comp won in {} guesses!".format(my_num, num_of_guess))
		return

	if mid > my_num:
		mid = (mid + max)/2
		binary_search(mid)
		num_of_guess += 1

	if mid < my_num:
		mid = (mid + min)/2
		binary_search(mid)
		num_of_guess += 1

def game():
		max = 10
		min = 1

		binary_search(int(max/2))

game()





