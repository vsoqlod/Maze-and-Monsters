import easy_troll
import easy_ogre
import easy_goblin
import enemy_factory
import random

class BeginnerFactory(enemy_factory.EnemyFactory):
  """Represent the factory that generates easier enemies. """
  def create_random_enemy(self):
    """Randomizes a monster to create"""
    monster = random.choice([easy_troll.EasyTroll(), easy_ogre.EasyOgre(), easy_goblin.EasyGoblin()])
    return monster

    
  