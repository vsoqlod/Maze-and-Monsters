import entity
import random

class EasyOgre(entity.Entity):
  """Represents enemy easy ogre"""
  def __init__(self):
    """Initializes randomized max_hp of the ogre by super()"""
    max_hp = random.randint(3, 5)
    super().__init__('Ogre', max_hp)
  def attack(self, entity):
    """The enemy attacks the hero - randomize the damage between 1-4. The hero should take the damage and a string representing the event should be returned."""
    damage = random.randint(1, 4)
    entity.take_damage(damage)
    return self._name + ' attacks ' + entity.name + ' for ' + str(damage) + " damage."