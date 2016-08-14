import sys
import random

def play():
	the_map = set_map()
	player_point = starting_player_location(the_map)
	monster_point = monster_location(the_map)
	print(player_point)
	move_up(player_point)
	print(player_point)
	# if player_point == (5, 5):
	# 	print("You win!")
	# 	return

def set_map():
	return [(1, 2, 3, 4, 5), (1, 2, 3, 4, 5)]

def starting_player_location(the_map):
	return random.choice(the_map[0]), random.choice(the_map[1])

def monster_location(the_map):
	return random.choice(the_map[0]), random.choice(the_map[1])

def move_up(player_point):
	new_location = list(player_point)
	if new_location[0] > 5:
		print('You lose!')
		end_game()
	return tuple(new_location)
def end_game():
	sys.exit()

play()
