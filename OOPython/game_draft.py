from character import Character
from monster import Dragon
from monster import Troll
from monster import Goblin
import sys


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
        monster_attack = self.monster.attack()
        if monster_attack:
            player_action = input("Monster is attacking! Do you want to dodge?: ")
            dodge_roll = self.player.dodge()
            # If so, see if dodge is successful
            if dodge_roll:
                print("Congrats, you dodged the monster's attack! Your turn now")
                self.player_turn()
            # If not, remove 1 player hit_point
            if dodge_roll is False:
                print("Ouch! You got hit! You lose 1 HP")
                self.player.hit_points -= 1
        # If monster isn't attacking, tell the player
        if monster_attack is False:
            print("The monster let you off easy and didn't attack. Your turn!")

    def player_turn(self):
        # Let the player attack, rest or quit
        player_action = input("Would you like to [A]ttack, [R]est or [Q]uit?: ").lower()
        # If they attack:
        if player_action == 'a':
            # See if attack is successful
            attack_roll = self.player.attack()
            if attack_roll:
                # If so, see if monster dodges
                monster_dodge_roll = self.monster.dodge()
                if monster_dodge_roll:
                    # If dodged, print that
                    print("Whoops, monster dodged your attack! His turn")
                    # If not dodged, subtract hit points from monster
                if monster_dodge_roll is False:
                    print("Nice, you landed your attack!")
            # If attack unsuccessful, tell player
            if attack_roll is False:
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
        if self.monster.hit_points == 0:
            # Add to the player's XP
            self.player.experience += 1
            # Print a message
            print("Congrats! You defeated the monster")
            # Get a new monster
            new_monster = self.monsters.pop()
            print("Here comes your new monster, a {}!".format(new_monster))

    def __init__(self):
        self.setup()
        while self.player.hit_points and (self.monster or self.monsters):
            print(self.player)
            self.monster_turn()
            self.player_turn()
            self.cleanup()

        if self.player.hit_points:
            print("You win!")
        if self.monsters or self.monster:
            print("You lose!")
