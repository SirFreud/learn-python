import sys

from character import Character
from monster import Dragon
from monster import Troll
from monster import Goblin


class Game(object):

    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop()
        except IndexError:
            return None

    def monster_turn(self):
        # Check to see if monster attacks
        if self.monster.attack():
            player_action = input("{} is attacking! Do you want to dodge? Y/n: ".format(self.monster)).lower()
            if player_action == 'y':
            # If so, see if dodge is successful
                if self.player.dodge():
                    print("Congrats, you dodged the monster's attack! Your turn now")
                    self.player.hit_points
            # If not, remove 1 player hit_point
                else:
                    print("Ouch! You got hit! You lose 1 HP")
                    self.player.hit_points -= 1
            if player_action == 'n':
                print("{} hit you for one 1 HP".format(self.monster))
                self.player.hit_points -= 1
        # If monster isn't attacking, tell the player
        else:
            print("The {} let you off easy and didn't attack. Your turn!".format(self.monster))

    def player_turn(self):
        # Let the player attack, rest or quit
        player_action = input("Would you like to [A]ttack, [R]est or [Q]uit?: ").lower()
        # If they attack:
        if player_action == 'a':
            # See if attack is successful
            print("You're attacking {}".format(self.monster))
            if self.player.attack():
                # If so, see if monster dodges
                if self.monster.dodge():
                    # If dodged, print that
                    print("Whoops, {} dodged your attack! His turn".format(self.monster))
                    # If not dodged, subtract hit points from monster
                else:
                    if self.player.levelup():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1
                    print("Nice, you hit {} with your {}!".format(
                        self.monster, self.player.weapon))
            # If attack unsuccessful, tell player
            else:
                print("Yikes, you missed the monster. His turn")
        # If they rest:
        elif player_action == 'r':
            # Call player.rest() method
            self.player.rest()
        # If they quit:
        elif player_action == 'q':
            # Exit the game
            print("Bye now!")
            sys.exit()
        # If they pick anything else:
        else:
            # Re-run this method
            self.player_turn()

    def cleanup(self):
        # If the monster HP = 0
        if self.monster.hit_points <= 0:
            # Add to the player's XP
            self.player.experience += self.monster.experience
            # Print a message
            print("Congrats! You defeated the {}".format(self.monster))
            # Get a new monster
            self.monster = self.get_next_monster()
            print("Here comes your new monster, a {}!".format(self.monster))

    def __init__(self):
        self.setup()
        while self.player.hit_points and (self.monster or self.monsters):
            print('\n' + '='*20)
            print(self.player)
            self.monster_turn()
            print('-'*20)
            self.player_turn()
            self.cleanup()
            print('\n' + '='*20)

        if self.player.hit_points:
            print("You win!")
        elif self.monsters or self.monster:
            print("You lose!")
        sys.exit()
