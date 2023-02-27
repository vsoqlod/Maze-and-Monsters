class Map:
  _instance = None
  _initialized = False
  """The map of the dungeon maze"""
  def __new__(cls):
    """In the event that the map has not been constructed, then it should be constructed, stored in the instance class variable, and returned."""
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    """Initializes the map to load map 1"""
    if not Map._initialized:
      self.load_map(1)
      Map._initialized = True

  def load_map(self, map_num):
    """Pass the integer for leveling the map and reset the 2D reveal list."""
    if map_num == 1:
      self._file = open("map1.txt")
    elif map_num == 2:
      self._file = open("map2.txt")
    elif map_num == 3:
      self._file = open('map3.txt')
    self._map = []
    self._revealed = []
    for row in self._file:
      characters = row.strip().split(" ")
      for char in characters: 
        self._map.append([row for row in char])
        self._revealed = [[False for x in range(len(self._map[0]))]for y in range(len(self._map))]
  
  def __getitem__(self, row):
    """The overloaded [] operator returns the specified row from the map."""
    return self._map[row]

  def __len__(self):
    """returns the number of rows in the map list.(Note: if you need to know the number of columns, use len(m), otherwise use len(m[r]))"""
    return len(self._map)

  def show_map(self, loc):
    """The map is returned as a string in the form of a 5x5 matrix, where revealed locations are represented by characters from the map, unrevealed locations are represented by letters, and the hero's location is represented by a star."""
    string = ''
    for row in range(5):
      for col in range(5):
        if row == loc[0] and col == loc[1]:
          string += '* '
        elif self._revealed[row][col] is True:
          string += self._map[row][col] + ' '
        else:
          string += 'x '
      string += '\n'
    return string 
      
  def reveal(self, loc):
    """Overwrites the character in the map list at the specified location with an ‘n’."""
    self._revealed[loc[0]][loc[1]] = True 

  def remove_at_loc(self, loc):
    """remove the location with 'n' where character modifies the situation."""
    self._map[loc[0]][loc[1]] = 'n' 
    

    

