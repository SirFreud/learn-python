import random

def main():
	the_map = set_map()
	player_point = starting_player_location(the_map)
	print(player_point)

def set_map():
	return [(1, 2, 3, 4, 5), (1, 2, 3, 4, 5)]

def starting_player_location(the_map):
	return random.choice(the_map[0]), random.choice(the_map[1])


main()

