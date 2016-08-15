from combat import Combat


# Creating a class for my character
class Character(Combat):
    experience = 0
    hit_points = 10

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

        for key, value in kwargs.items():
            setattr(self, key, value)
