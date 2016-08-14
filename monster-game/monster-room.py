import sys
import random

def play():

	print("""Welcoem to the Mosnter Room! You've been dropped into a 5x5 grid.\n
	Your goal is to reach the upper right hand corner at location (5, 5)\n
	You'll start in a random location\n
	Watch out! A monster lurks in a random location on the grid.\n
	If you run into him, you'll die\n
	You can type any direction you'd like to move: UP, DOWN, LEFT or RIGHT\n
	Type SHOW LOCATION to find out where on the grid you are.\n
	Good luck!
	""")

	the_map = set_map()
	player_point = starting_player_location(the_map)
	monster_point = monster_location(the_map)



	if player_point == monster_point:
		print("You got eaten by the monster, you lose!")
		end_game()

	# if player_point == (5, 5):
	# 	print("You win!")
	# 	return

def set_map():
	return [(1, 2, 3, 4, 5), (1, 2, 3, 4, 5)]

def starting_player_location(the_map):
	return [random.choice(the_map[0]), random.choice(the_map[1])]

def monster_location(the_map):
	return [random.choice(the_map[0]), random.choice(the_map[1])]

def move_up(player_point):
	if player_point[0] == 5:
		print('You fell off the map! You lose!')
		end_game()
	player_point[0] += 1
	return player_point
def end_game():
	sys.exit()


play()