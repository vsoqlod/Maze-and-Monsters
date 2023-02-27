import abc 
class Entity(abc.ABC):
  """Abstract class - describes a character in the game
  Attribute:
    take_damage(self, dmg)
    heal(setf)
    _str_ (setf): string
    <abstract> attack(self, entity)"""
  def __init__(self, name, max_hp = 25):
    """The instance variables are initialized"""
    self._name = name
    self._max_hp = max_hp
    self._hp = max_hp

  def take_damage(self, dmg):
    """Subtracts the damage from the HP, but does not allow the HP to fall below zero"""
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0
  
  def heal(self):
    """The entity's HP is restored to max_hp"""
    self._hp = self._max_hp
  
  def __str__(self):
    """The function returns a string with the format 'Name/nHP: hp/max_hp'."""
    return "\n" + self.name + "\n" + "HP: "+ str(self._hp) + "/" + str(self._max_hp)

  @property
  def name(self):
    """The function helps to get name"""
    return self._name

  @property
  def hp(self):
    """The function helps to get the HP"""
    return self._hp
    
  @abc.abstractmethod
  def attack(self, entity):
    """In order to attack and damage the opposing entity, all entity subclasses must override an abstract method (no code)."""
    pass
  