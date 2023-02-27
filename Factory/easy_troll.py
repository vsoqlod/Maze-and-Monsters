import entity
import random

class EasyTroll(entity.Entity):
  """Represents enemy easy Troll"""
  def __init__(self):
    """Initializes randomized max_hp of the troll by super()"""
    max_hp = random.randint(4, 5)
    super().__init__('Troll', max_hp)
  def attack(self, entity):
    """The enemy attacks the hero - randomize the damage between 1-5. The hero should take the damage and a string representing the event should be returned."""
    damage = random.randint(1, 5)
    entity.take_damage(damage)
    return self._name + ' attacks ' + entity.name + ' for ' + str(damage) + " damage."