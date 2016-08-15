from combat import Combat
import random


# Creating a class for my character
class Character(Combat):
    attack_limit = 10
    experience = 0
    base_hit_points = 10

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if self.weapon == 'sword':
            roll += 1
        if self.weapon == 'axe':
            roll += 2
        return roll > 4

# Group common operations into functions
# Group common functionality into classes
    def get_weapon(self):
        weapon_choice = input("Weapon? ([S]word, [A]xe, [B]ow: ").lower()
        if weapon_choice in 'sab':
            if weapon_choice == 's':
                return 'sword'
            if weapon_choice == 'a':
                return 'axe'
            if weapon_choice == 'b':
                return 'bow'
        else:
            return self.get_weapon()

    def __init__(self, **kwargs):
        self.name = input("Name your character: ")
        self.weapon = self.get_weapon()
        self.hit_points = self.base_hit_points

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{}, HP: {}, XP: {}'.format(
            self.name, self.hit_points, self.experience)

    def rest(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points += 1

    def levelup(self):
        return self.experience >= 5
