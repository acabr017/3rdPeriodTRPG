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
class weapon(items): #ranged and melee can be in the same class, just that melee would have higher accuracy to hit
  def __init__(self, name, type, rarity, damage, accuracy, elemental):
    super().__init__(name, type, rarity)
    self.type = "weapon"
    self.dmg = damage
    self.acc = accuracy
    self.ele = elemental
    #potential melee weapon ideas: rusty sword (starting weapon), basic sword, longsword, rapier, axe, dual axe, fire sword(?), spear, poison tipped sword or spear(?), super cool omega gamer blade of greatness (strongest sword in game)
    #potential ranged weapon ideas: old bow (starting weapon), basic bow, crossbow, dynamite(?), poison darts, throwing knives, gun (final ranged weapon)
class potion(items): #there are 2 main types of potions: 1 for healing and 1 for mana. There'll be mini potions that grant only half the boost of a normal potion.
  def __init__(self, name, type, rarity, health_boost, mana_boost)
  super().__init__(name, type, rarity)
  self.type = "potion"
  self.hb = health_boost
  self.mb = mana_boost

class armor(items): #armor can be equipped and grants the player a defense boost. could grant an attack boost?
  def __init__(self, name, type, rarity, defense)
  super().__init__(name, type, rarity)
  self.type = "armor"
  self.def = defense
  #armor:rusty chainmail, chainmail, knight armor, palladin armor, etc...............
class spell(items): #like ranged weapons, spells will have a decent chance to miss.
  def __init__(self, name, type, rarity, damage, mana_cost, ):
  super().__init__(name, type, rarity)
  self.type = spell
  self.damage = damage
  self.acc = accuracy
  self.ele = elemental
  self.mana_cost = mana_cost
  #spells: fire blast, fireball, ice spike, freeze, poison
