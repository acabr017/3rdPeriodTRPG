import random
from weapon import Weapon


class Character:
    """
    This is the parent class of all characters.
    Player characters and Enemies will extended this class and
    be child classes.
    """

    def __init__(
        self,
        name,
        strength,
        dexterity,
        health,
        luck,
        intelligence,
        defense,
        weapon=None,
    ):
        self.name = name
        self.str = strength
        self.dex = dexterity
        self.hp = health * 8
        self.luck = luck
        self.int = intelligence
        self.defense = defense
        self.equipped_weapon = weapon
        self.att_stat = max((self.str, self.dex, self.int))

    def level_up(self):
        stats = sorted([self.dex, self.str, self.defense, self.int, self.luck, self.hp])

    def __str__(self):
        return f"Name: {self.name} \n \
            Strength: {self.str} \n \
            Dexterity: {self.dex} \n \
            Defense: {self.defense} \n \
            Health: {self.hp} \n \
            Intelligence: {self.int} \n \
            Luck: {self.luck} \n \
            Equipped Weapon: {self.equipped_weapon} \
        "

    def _do_damage(self) -> int:
        if self.equipped_weapon is None:
            weapon_damage = self.att_stat
        else:
            weapon_damage = self.equipped_weapon.dmg
        return random.randint(weapon_damage, (self.att_stat + weapon_damage))

    def _does_it_hit(self, attack, defense):
        if attack > defense:
            return True
        return False

    def attack(self, enemy):
        self_attack = self.att_stat + random.randint(0, self.luck)
        enemy_defense = enemy.defense + random.randint(0, enemy.luck)
        if self._does_it_hit(self_attack, enemy_defense):
            self._do_damage()
        else:
            print("Your attack misses! You do 0 points of damage!")


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
        self.hp = 7 * 8
        self.dex = 5
        self.luck = 4
        self.int = 3
        self.att_stat = self.str
        self.equipped_weapon = Weapon(5, 5, None, None, "common", "sword")


class Ranger(Character):
    """
    Ranger class that will extend the Character class.
    Starting Weapon: Bow and Arrows
    Starting Spells: True Strike (increases chance to hit)
    """

    def __init__(self, name):
        self.name = name
        self.str = 3
        self.defense = 5
        self.hp = 4 * 8
        self.dex = 10
        self.luck = 8
        self.int = 7
        self.att_stat = self.dex
        self.equipped_weapon = Weapon(5, 5, None, None, "common", "bow")


class Mage(Character):
    """
    Ranger class that will extend the Character class.
    Starting Weapon: Bow and Arrows
    Starting Spells: True Strike (increases chance to hit)
    """

    def __init__(self, name):
        self.name = name
        self.str = 4
        self.defense = 5
        self.hp = 3 * 8
        self.dex = 6
        self.luck = 8
        self.int = 10
        self.att_stat = self.dex
        self.equipped_weapon = Weapon(5, 5, None, None, "common", "bow")
