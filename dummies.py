import random


class Weapon:
    def __init__(self, damage, accuracy, status_effect, elemental, rarity, type):
        self.type = type
        self.dmg = damage
        self.acc = accuracy
        self.stat_effect = status_effect
        self.elemental_type = elemental
        self.rarity = rarity

    def __str__(self):
        return f"{self.type} \n\
            \t\t      Damage: {self.dmg} \n \
            \t\t      Accuracy: {self.acc} \n \
            \t\t      Stat Effects: {self.stat_effect} \n \
            \t\t      Element: {self.elemental_type} \n \
            \t\t      Rarity: {self.rarity}"


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
        self.hp = health * 10
        self.luck = luck
        self.int = intelligence
        self.defense = defense
        self.equipped_weapon = weapon

    def __str__(self):
        return f"Name: {self.name} \n \
            Strength: {self.str} \n \
            Dexterity: {self.dex} \n \
            Defense: {self.defense} \n \
            Health: {self.hp} \n \
            Intelligence: {self.int} \n \
            Luck: {self.luck} \n \
            Equipped Weapn: {self.equipped_weapon} \
        "

    def _do_damage(self, weapon_dmg) -> int:
        return random.randint(weapon_dmg, weapon_dmg)

    def _does_it_hit(self, my_def):
        pass

    def attack(self, enemy):
        self_attack = max(self.str, self.dex) + random.randint(0, self.luck)
        enemy_defense = enemy.defense + random.randint(0, enemy.luck)
        weapon_damage = self.equipped_weapon.dmg
        if self_attack > enemy_defense:
            dmg = self._do_damage(weapon_damage)
            print(f"You do {dmg} point(s) of damage!")
        else:
            print("You miss and do no damage!")


class Item:
    def __init__(self, name, type, rarity):
        self.name = name
        self.type = type
        self.rarity = rarity


class Potion:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect


# let's make some easy dummies

fire_potion = Potion("fire potion", "no fire")
player_sword = Weapon(4, 4, None, None, "common", "sword")
player_character = Character("Player", 5, 5, 5, 5, 5, 5, player_sword)
enemy_sword = Weapon(3, 3, None, None, "common", "Sword")
enemy_character = Character("Enemy", 3, 3, 3, 3, 3, 3, enemy_sword)
sample_item = Item("Potion", "potion", "common")

if fire_potion.effect == "no fire":
    print("You douse the flames")
    # check the player status to see if they are on fire and then turn it off
