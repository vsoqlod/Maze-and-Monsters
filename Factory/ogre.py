import entity
import random

class Ogre(entity.Entity):
  """Represent enemy, Ogre"""
  def __init__(self):
    """initialize randomized max_hp by super() of horrifying Ogre."""
    max_hp = random.randint(8, 12)
    super().__init__('Horrifying Ogre', max_hp)

  def attack(self, entity):
    """The enemy attacks the hero - randomize the damage between 6-10. The hero should take the damage and a string representing the event should be returned."""
    damage = random.randint(6, 10)
    entity.take_damage(damage)
    return self._name + ' attacks ' + entity.name + ' for ' + str(damage) + " damage."