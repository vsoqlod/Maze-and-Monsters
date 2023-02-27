"""
Gabriel Quezada, Thuan Nguyen, Jae Bum Jang
Fall 2022, 11/17
Lab 12 - Group 17

This is a program that allows players to enter a maze and battle various monsters as they encounter while exploring. The user will continue to go through the maze and progress to new levels as they find the finish.
"""
import hero
import map
import check_input
import random
import beginner_factory
import expert_factory


def main():
  """Prompting the user enters their name. Create a loop which repeats until the hero dies or quits the game. Provide a menu that allows the player to choose which direction to move in (north, south, east, west), move the hero in that direction, reveal the encounter, and if its a monster use the Factory Method to generate a random monster, goes to next level after finding the finish then present next level map."""
  name_trav = input("What is your name, traveler? ")
  traveler = hero.Hero(name_trav)
  choice = 0
  board = map.Map()
  location = ''
  choose_difficulty = check_input.get_int_range('Difficulty:\n1. Beginner\n2. Expert\n', 1, 2)
  count = 1
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
    elif choice == 5:
      print('Game Over.')
      break
    board.reveal(traveler.loc)

    if location == 'x':
      print('You cannot go that way...')

    elif location == 'm':
      if choose_difficulty == 1:
        monster = beginner_factory.BeginnerFactory().create_random_enemy()
      elif choose_difficulty == 2:
        monster = expert_factory.ExpertFactory().create_random_enemy()
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
        if choice_att == 2:
          print("You ran away!")
          in_bounds = 'x'
          while in_bounds == 'x':
            move = random.randint(1, 4)
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
    elif board[traveler.loc[0]][traveler.loc[1]] == 's':
      print('You are back to where you began. Head forward to the finish.')
    elif location == 'i':
      if traveler.hp < 25:
        print(
          "You found a Health Potion! You drink it to restore your health.")
        traveler.heal()
        board.remove_at_loc(traveler.loc)
      elif traveler.hp == 25:
        print(
          'You are at full health! You find a Health Potion and leave it for later.'
        )
    elif location == 'f':
      print('Congratulations! You found the stairs to the next floor of the dungeon.')
      count += 1
      if count == 4:
        count = 1
      if count == 1:
        board.load_map(1)
      elif count == 2:
        board.load_map(2)
      elif count == 3:
        board.load_map(3)
    
  if traveler.hp == 0:
    print('You have been slain.')


main()
