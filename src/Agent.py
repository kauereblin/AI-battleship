import random, pygame
from time import sleep
from Ship import Ship
from constants import *
from util import *

class Agent:
  ships = []
  moves = []

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

      new_ship = Ship(positions, size, orientation)
      self.ships.append(new_ship)
      idx -= 1
    
  def update(self) -> None:
    pass

  def draw(self, surface) -> None:
    pass
    # for ship in self.ships:
    #   for x, y in zip(ship.positions["x"], ship.positions["y"]):
    #     rec = pygame.Rect(x * CELL_WIDTH, y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
    #     pygame.draw.rect(surface, RED, rec)
