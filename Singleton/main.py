"""
Gabriel Quezada, Thuan Nguyen, Jae Bum Jang
Fall 2022, 11/11
Lab 11 - Group 17

This is a program that allows players to enter a maze and battle monsters as they encounter while exploring. The user will win if they survives and finds the exit of the maze.
"""
import hero
import enemy
import map
import check_input
import random

def main():
  """Prompting the user enters their name. Create a loop which repeats until the hero dies, finds the finish, or quits the game. Provide a menu that allows the player to choose which direction to move in (north, south, east, west), move the hero in that direction, reveal the encounter, and reveal the encounter."""
  name_trav = input("What is your name, traveler? ")
  traveler = hero.Hero(name_trav)
  choice = 0
  board = map.Map()
  location = ''
  
  while traveler.hp > 0 and choice != 5:
    board.reveal(traveler.loc)
    print(traveler)
    print(board.show_map(traveler.loc))
    print('1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit')
    choice = check_input.get_int_range('Enter choice: ', 1, 5)
    if choice == 1:
      location = traveler.go_north()
    elif choice == 2:
      location = traveler.go_south()
    elif choice == 3:
      location = traveler.go_east()
    elif choice == 4:
      location = traveler.go_west()
    board.reveal(traveler.loc)

    if location == 'x':
      print('You cannot go that way...')
    
    elif location == 'm':
      monster = enemy.Enemy()
      print(f'You encounter a {monster.name}\n{monster}')
      choice_att = 0
      while traveler.hp > 0 and monster.hp > 0 and choice_att != 2:
        print(f"1. Attack {monster.name}\n2. Run Away")
        choice_att = check_input.get_int_range("Enter choice: ", 1, 2)
        if choice_att == 1:
          print(traveler.attack(monster))
          if monster.hp > 0:
            print(monster.attack(traveler))
          else: 
            print(f"You have slain a {monster.name}")
            board.remove_at_loc(traveler.loc)
        if choice_att  == 2:
          print("You ran away!")
          in_bounds = 'x'
          while in_bounds == 'x':
            move = random.randint(1,4)
            if move == 1:
             in_bounds = traveler.go_west()
            elif move == 2:
              in_bounds = traveler.go_east()
            elif move == 3:
              in_bounds = traveler.go_south()
            elif move == 4:
              in_bounds = traveler.go_north()

    elif location == 'n':
      print('There is nothing here...')
    elif board[traveler.loc  [0]][traveler.loc[1]] == 's':
      print('You are back to where you began. Head forward to the finish.')
    elif location == 'i':
      if traveler.hp < 25:
        print("You found a Health Potion! You drink it to restore your health.")
        traveler.heal()
        board.remove_at_loc(traveler.loc)
      elif traveler.hp == 25:
        print('You are at full health! You find a Health Potion and leave it for later.')
    elif location == 'f':
      print('Congratulations! You found the exit.')
      print('Game Over.')
      choice = 5
  if traveler.hp == 0:
    print('You have been slain.')



main()