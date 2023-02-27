import entity
import random

class EasyGoblin(entity.Entity):
  """Represents enemy easy goblin"""
  def __init__(self):
    """Initializes randomized max_hp of the goblin by super()"""
    max_hp = random.randint(3, 4)
    super().__init__('Goblin', max_hp)

  def attack(self, entity):
    """The enemy attacks the hero - randomize the damage between 1-3. The hero should take the damage and a string representing the event should be returned."""
    damage = random.randint(1, 3)
    entity.take_damage(damage)
    return self._name + ' attacks ' + entity.name + ' for ' + str(damage) + " damage."
    