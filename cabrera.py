import random


class Character:
    """
    This is the parent class of all characters.
    Player characters and Enemies will extended this class and
    be child classes.
    """

    def __init__(self, name, strength, dexterity, health, luck, intelligence, defense):
        self.name = name
        self.str = strength
        self.dex = dexterity
        self.hp = health * 10
        self.luck = luck
        self.int = intelligence
        self.defense = defense
        self.equipped_weapon = None

    def __str__(self):
        return f"Name: {self.name} \n \
            Strength: {self.str} \n \
            Dexterity: {self.dex} \n \
            Defense: {self.defense} \n \
            Health: {self.hp} \n \
            Intelligence: {self.int} \n \
            Luck: {self.luck} \n \
        "

    def _do_damage(self, weapon_dmg) -> int:
        return random.randint(1, weapon_dmg)
    
    def _does_it_hit(self,nmy_def)

    def attack(self, enemy):
        self_attack = max(self.str, self.dex) + random.randint(0, self.luck)
        enemy_defense = enemy.defense + random.randint(0, enemy.luck)
        weapon_damage = 6  # In the future, weapon.damage
        if self_attack > enemy_defense:
            dmg = self._do_damage(weapon_damage)
            print(f"You do {dmg} point(s) of damage!")
        else:
            print("You miss and do no damage!")


class Warrior(Character):
    """
    Warrior class that will extend the Character class.
    Starting Weapon: The Sword
    Starting Spells: None
    """

    def __init__(self, name):
        self.name = name
        self.str = 10
        self.defense = 8
        self.hp = 7 * 6
        self.dex = 5
        self.luck = 4
        self.int = 3
        self.equipped_weapon = "Sword"
        

class Ranger(Character):
    """
    Ranger class that will extend the Character class.
    Starting Weapon: Bow and Arrows
    Starting Spells: True Strike (increases chance to hit)
    """

    def __init__(self, name):
        self.name = name
        self.str = 10
        self.defense = 8
        self.hp = 7 * 6
        self.dex = 5
        self.luck = 4
        self.int = 3
        self.equipped_weapon = "Sword"
