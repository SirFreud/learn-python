import sys
import random


def play():
    open_dialog()
    the_map = set_map()
    player_point = starting_player_location(the_map)
    monster_point = monster_location(the_map)

    while True:
        user_input = input("\n>> ".lower())
        if user_input == "SHOW LOCATION".lower():
            show_location(user_input, player_point)
        if user_input == "UP".lower():
            move_up(player_point)
        if user_input == "DOWN".lower():
            move_down(player_point)
        if user_input == "LEFT".lower():
            move_left(player_point)
        if user_input == "RIGHT".lower():
            move_right(player_point)
        if user_input == 'QUIT'.lower():
            end_game()
        if player_point == monster_point:
            print("You got eaten by the monster, you lose!")
            end_game()
        if player_point == [5, 5]:
            print("Congratulations! You win!")
            play_again = input(("Would you like to play again? Y/n: ".lower()))
            if play_again == 'y':
                play()
            else:
                end_game()


def set_map():
    return [(1, 2, 3, 4, 5), (1, 2, 3, 4, 5)]


def starting_player_location(the_map):
    return [random.choice(the_map[0]), random.choice(the_map[1])]


def monster_location(the_map):
    return [random.choice(the_map[0]), random.choice(the_map[1])]


def show_location(user_input, player_point):
    if user_input == 'show location'.lower():
        print(tuple(player_point))


def move_up(player_point):
    if player_point[1] == 5:
        print('You fell off the map! You lose!')
        end_game()
    player_point[1] += 1
    return player_point


def move_down(player_point):
    if player_point[1] == 0:
        print('You fell off the map! You lose!')
        end_game()
        player_point[1] += 0
    return player_point


def move_right(player_point):
    if player_point[0] == 5:
        print('You fell off the map! You lose!')
        end_game()
    player_point[0] += 1
    return player_point


def move_left(player_point):
    if player_point[0] == 0:
        print('You fell off the map! You lose!')
        end_game()
    player_point[0] -= 1
    return player_point


def end_game():
    print("Bye!")
    sys.exit()


def open_dialog():
    print("""
    \nWelcome to the Mosnter Room! You've been dropped into a 5x5 grid.\n
    Your goal is to reach the upper right hand corner at location (5, 5)\n
    You'll start in a random location\n
    Watch out! A monster lurks in a random location on the grid.\n
    If you run into him, you'll die\n
    You can type any direction you'd like to move: UP, DOWN, LEFT or RIGHT\n
    Type SHOW LOCATION to find out where on the grid you are.\n
    If you run to a point off of the grid, you'll fall off!\n
    Type QUIT to quit the game\n
    Good luck!
    """)

play()
