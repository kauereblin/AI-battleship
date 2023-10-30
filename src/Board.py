# import pygame
import os

from Ship import Ship
from constants import *

class Board:
  def __init__(self) -> None:
    pass

  def draw_placement(self, ships: list[Ship]) -> None:
    os.system("cls")
    for col_cell in range(GRID_SIZE):
      print()
      for row_cell in range(GRID_SIZE):
        empty = True

        for ship in ships:
          printed = False
          for coord_ship in ship.positions:
            if (coord_ship[0] == row_cell and coord_ship[1] == col_cell):
              empty = False
              printed = True
              break
          if (printed):
            break

        if (empty):
          print(" - ", end="")
        else:
          print(" N ", end="")

  def draw_moves(self, moves: list[int]) -> None:
    print("\n------------------")
    for col_cell in range(GRID_SIZE):
      print()
      for row_cell in range(GRID_SIZE):
        empty = True

        for coord_shot in moves:
          if (coord_shot[0] == row_cell and coord_shot[1] == col_cell):
            empty = False
            if (coord_shot[2]):
              print(" X ", end="")
            else:
              print(" O ", end="")
            break
        
        if (empty):
          print(" - ", end="")
