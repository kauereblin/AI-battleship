import random, pygame
from time import sleep
from Ship import Ship
from constants import *
from util import *

class Agent:
  ships = []
  moves = []
  targets = []

  def __init__(self) -> None:
    self.set_ships()

  def set_ships(self) -> None:
    idx = len(SHIP_SIZES) - 1
    while idx >= 0:
      size = SHIP_SIZES[idx]
      orientation = random.randint(0, 1)

      positions = []
      if orientation == 0: # horizontal
        x = random.randint(0, GRID_SIZE - size)
        y = random.randint(0, GRID_SIZE - 1)
        positions = [[x + _, y] for _ in range(size)]
      else: # vertical
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - size)
        positions = [[x, y + _] for _ in range(size)]

      if hasShipConflict(positions, self.ships):
        continue

      #print(positions)
      new_ship = Ship(positions, size, orientation)
      self.ships.append(new_ship)
      idx -= 1

  def guess_random(self):
    while True:
      guess_row, guess_col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
      if [guess_row, guess_col] not in self.moves:
        break
    
    return [guess_row, guess_col]

  def update(self, player_ships) -> None:
    if not self.targets:
      guess_row, guess_col = self.guess_random()
    else:
      guess_row, guess_col = self.targets.pop()

    if (hasShipConflict([[guess_row, guess_col]], player_ships)):
      potential_targets = [[guess_row + 1, guess_col], [guess_row, guess_col + 1],
                         [guess_row - 1, guess_col], [guess_row, guess_col - 1]]
      
      for move_x, move_y in potential_targets:
        if (0 <= move_x < GRID_SIZE - 1 and 0 <= move_y < GRID_SIZE - 1 and \
            [move_x, move_y] not in self.moves and [move_x, move_y] not in self.targets):
          self.targets.append([move_x, move_y])
    
    self.moves.append([guess_row, guess_col])
