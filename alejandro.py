# This is where Alejandro will provide his parts of the project.
class items:
  def __init__(self, name, type, rarity):
    # damage accuracy and elemental reserved for weapons
    # defense reserved for armor
    # health_boost and mana_boost reserved for potions
    self.name = name
    self.type = type
    self.rarity = rarity


  def __str__(item):
     return f"Item Name: {self.name} \n \
              Type: {self.type} \n \
              Rarity: {self.rar} \n \
            "
class weapon(items):
  def __init__(self, name, type, rarity, damage, accuracy, elemental):
    super().__init__(name, type, rarity)
    self.type = "weapon"
    self.dmg = damage
    self.acc = accuracy
    self.ele = elemental

class potion(items):
  def __init__(self, name, type, rarity, health_boost, mana_boost)
  super().__init__(name, type, rarity)
  self.type = "potion"
  self.hb = health_boost
  self.mb = mana_boost

class armor(items):
  def __init__(self, name, type, rarity, defense)
  super().__init__(name, type, rarity)
  self.type = "armor"
  self.def = defense
  
class spell(items):
  def __init__(self, name, type, rarity, damage, mana_cost, ):
  super().__init__(name, type, rarity)
  self.type = spell
  self.damage = damage
  self.mana_cost = mana_cost
