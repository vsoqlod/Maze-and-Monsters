import entity
import random

class Goblin(entity.Entity):
  "Represents enemy goblin"
  def __init__(self):
    """Initializes randomized max_hp of the Hob Goblin by super()"""
    max_hp = random.randint(6, 10)
    super().__init__('Hob Goblin', max_hp)

  def attack(self, entity):
    """The enemy attacks the hero - randomize the damage between 4-8. The hero should take the damage and a string representing the event should be returned."""
    damage = random.randint(4, 8)
    entity.take_damage(damage)
    return self._name + ' attacks ' + entity.name + ' for ' + str(damage) + " damage."