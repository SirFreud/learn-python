def show_list(item_list):
	for item in item_list:
		print(item)

def add_to_list(item_list, new_item):
	item_list.append(new_item)
	print("Added {}. List now has {} items.\n".format(new_item, len(item_list)))

def get_help():
	print("Type SHOW to print the list")
	print("Type DONE to quit")
	print("Type HELP to see this message again\n")

get_help()

def main():
	item_list = []
	user_input = ""
	while True:
		user_input = input("What would you like to buy?: ")
		if user_input == "SHOW":
			show_list(item_list)
			continue
		if user_input == "HELP":
			get_help()
			continue
		if user_input == "DONE":
			break
		add_to_list(item_list, user_input)
	print("Here's your list: ")
	for item in item_list:
		print(item)

main()