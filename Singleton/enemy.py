import entity
import random
class Enemy(entity.Entity):
  """Extends entity - monster character that the hero encounters in the maze.
  Attribute:
    attack(self, entity): string"""
  def __init__(self):
    """A name is randomly selected from a list of names, and the monster's health is also randomly selected"""
    self._name = random.choice(['Goblin', 'Troll', 'Ghoul', 'Skeleton', 'Kobold'])
    self._max_hp = random.randint(4, 8)
    self._hp = self._max_hp

  def attack(self, entity):
    """The enemy attacks the hero - randomize the damage between 1-4. The hero should take the damage and a string representing the event should be returned."""
    damage = random.randint(1, 4)
    entity.take_damage(damage)
    return self._name + ' attacks ' + entity.name + ' for ' + str(damage) + " damage."