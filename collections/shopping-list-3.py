import sys

shopping_list = []

def show_help():
	print("\nSeparate each item with a comma")
	print("\nType DONE to quit, SHOW to see current list, or HELP to see this message")
def show_list():
	count = 1
	for item in shopping_list:
		print('{}. {}'.format(count, item))
		count += 1

print('Give me a list of things you would like to shop for')
show_help()

while True:
	new_stuff = input("> ")

	if new_stuff == 'DONE':
		print("\nHere's your list")
		show_list()
		break
	if new_stuff == 'HELP':
		show_help()
		continue
	if new_stuff == 'SHOW':
		show_list()
		continue
	new_list = new_stuff.split(',')
	index =input('Add this at a certain spot? Press Enter for the end of the list or give me a number. Currently {} items in the list\n'.format(len(shopping_list)))
	if index:
		try:
			spot = int(index) - 1
		except ValueError:
			print("That's not a number!")
			continue
		else:
			for item in new_list:
				shopping_list.insert(spot, item.strip())
				spot += 1
	else:
		for item in new_list:
			shopping_list.append(item.strip())


