from Ship import Ship

from constants import *

class Player():
  ships = []
  moves = []

  def __init__(self) -> None:
    pass

  def update(self, state) -> None:
    if (state == PLACING_SHIPS):
      first_coord = eval(input(f"\nDigite a posição do seu navio de tamanho {SHIP_SIZES[len(self.ships)]}: "))
      orientation = str(input("Digite a orientação do seu navio (h/v): "))

      if (orientation == "h"):
        positions = [[first_coord[0] + _, first_coord[1]] for _ in range(SHIP_SIZES[len(self.ships)])]
      else:
        positions = [[first_coord[0], first_coord[1] + _] for _ in range(SHIP_SIZES[len(self.ships)])]

      self.ships.append(Ship(positions, len(positions), orientation))

    elif (state == PLAYER_TURN):
      coord = eval(input("\nDigite a posição do seu tiro: "))
      self.moves.append(coord)
