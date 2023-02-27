import entity
import random

class Troll(entity.Entity):
  """Represent enemy, Troll"""
  def __init__(self):
    """Initializes randomized max_hp of the moutain troll by super()"""
    max_hp = random.randint(10, 14)
    super().__init__('Mountain Troll', max_hp)

  def attack(self, entity):
    """The enemy attacks the hero - randomize the damage between 8-12. The hero should take the damage and a string representing the event should be returned."""
    damage = random.randint(8, 12)
    entity.take_damage(damage)
    return self._name + ' attacks ' + entity.name + ' for ' + str(damage) + " damage."