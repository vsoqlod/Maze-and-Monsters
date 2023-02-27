import entity
import random
import map

class Hero(entity.Entity):
  """abstract class - describes a character in the game.
  Attribute:
    attack(self, entity): string
    go_north(self): char len_ (setf): int
    go_south(setf): char show_map(self, loc): string
    go_east(setf): char
    go_west(setf): char
  """
  def __init__(self, name):
    """Sets the hero's starting position to row=0, col=0, and initializes the name and max_hp using super."""
    super().__init__(name)
    self._loc = [0, 0]

  def attack(self, entity):
    """The hero attacks the enemy - randomly assign damage between 2 and 5, the enemy should take the damage, and the method should return a string representing the event."""
    damage = random.randint(2, 5)
    entity.take_damage(damage)
    return self._name + ' attacks a ' + entity._name + ' for ' + str(damage) + ' damage.'

  def go_north(self):
    """Update the hero's location by adding or subtracting 1 from the row or column, but only if it falls within the boundaries"""
    board = map.Map()
    if self._loc[0] > 0:
      self._loc[0] -= 1
      return board[self._loc[0]][self.loc[1]]
    else:
      return 'x'

  def go_south(self):
    """Update the hero's location by adding or subtracting 1 from the row or column, but only if it falls within the boundaries"""
    board = map.Map()
    if self._loc[0] < len(board) - 1:
      self._loc[0] += 1
      return board[self._loc[0]][self.loc[1]]
    else:
      return 'x'

  def go_east(self):
    """Update the hero's location by adding or subtracting 1 from the row or column, but only if it falls within the boundaries"""
    board = map.Map()
    if self._loc[1] < len(board[1]) - 1:
      self._loc[1] += 1
      return board[self._loc[0]][self.loc[1]]
    else:
      return 'x'

  def go_west(self):
    """Update the hero's location by adding or subtracting 1 from the row or column, but only if it falls within the boundaries"""
    board = map.Map()
    if self._loc[1] > 0:
      self._loc[1] -= 1
      return board[self._loc[0]][self.loc[1]]
    else:
      return 'x'
      
  @property
  def loc(self):
    """Function helps to get the location"""
    return self._loc