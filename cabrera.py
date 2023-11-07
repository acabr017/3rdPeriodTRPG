import random

class Character:
    """ 
    This is the parent class of all characters. 
    Player characters and Enemies will extended this class and 
    be child classes. 
    """

    def __init__(self,name,strength,dexterity,health,luck,intelligence,defense):
        self.name = name
        self.str = strength
        self.dex = dexterity
        self.hp = health
        self.luck = luck
        self.int = intelligence
        self.defense = defense
        self.equipped_weapon = None
        
    def __str__(self):
        return f"Name: {self.name} \n \\
            Strength: {self.strength} \n \\
            Dexterity: {self.dex} \n \\
            Defense: {self.defense} \n \\
            Health: {self.hp} \n \\
            Intelligence: {self.int} \n \\
            Luck: {self.luck} \n \\
        "
    
    def _do_damage(self,weapon:weapon)->int:
        pass


    def attack(self,enemy:Character):
        self_attack = max(self.str,self.dex) + random.randint(0,self.luck)
        enemy_defense = enemy.defense + random.randint(0,enemy.luck)
        if self_attack > enemy_defense:
            dmg = self._do_damage(self.equipped_weapon)
            print(f"You do {dmg} point(s) of damage!")
        else:
            print("You miss and do no damage!")



class Warrior(Character):
    """
    Warrior class that will extend the Character class. 
    """

    def __init__(self, name):
        self.name = name
        self.str = 10
        self.defense = 8
        self.hp = 7
        self.dex = 5
        self.luck = 4
        self.int = 3
        self.equipped_weapon = "Sword"
        

