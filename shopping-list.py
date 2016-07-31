def main():
	number_of_items = int(input("How many items would you like to buy?: "))
	item_list = insert_into_list(number_of_items)
	print(item_list)

def insert_into_list(number_of_items):
	list_of_items = []
	for i in range(0, number_of_items):
		user_input = input()
		list_of_items.append(user_input)
	return list_of_items

main()