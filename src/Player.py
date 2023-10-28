import pygame
from Ship import Ship

from constants import *

class Player():
  ships = []
  moves = []

  def __init__(self) -> None:
    pass

  def add_ship(self, positions, orientation) -> None:
    self.ships.append(Ship(positions, len(positions), orientation))

  def update(self) -> None:
    pass

  def draw(self, surface) -> None:
    for ship in self.ships:
      for x, y in zip(ship.positions["x"], ship.positions["y"]):
        rec = pygame.Rect(x * CELL_WIDTH, y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
        pygame.draw.rect(surface, GREEN, rec)
