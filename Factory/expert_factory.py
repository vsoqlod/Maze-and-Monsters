import troll
import ogre
import goblin
import enemy_factory
import random

class ExpertFactory(enemy_factory.EnemyFactory):
  """Represent the factory that generates more difficult enemies. """
  def create_random_enemy(self):
    """Randomizes a monster to create"""
    monster = random.choice([troll.Troll(), ogre.Ogre(), goblin.Goblin()])
    return monster