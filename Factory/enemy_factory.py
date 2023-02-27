import abc

class EnemyFactory(abc.ABC):
  """It is an abstract base factory interface for whole factory"""
  abc.abstractmethod
  def create_random_enemy(self):
    """method that create randomized enemies."""
    pass