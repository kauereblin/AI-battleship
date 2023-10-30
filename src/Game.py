from Agent import Agent
from Player import Player
from Board import Board

from constants import *
from util import *

class Game:
  running = True
  board = Board()
  agent = Agent()
  player = Player()
  state = PLACING_SHIPS

  def __init__(self) -> None:
    pass

  def run(self) -> None:
    while self.running:
      if (self.state == PLACING_SHIPS):
        self.player.update(self.state)
        self.board.draw_placement(self.player.ships)
        if (len(self.player.ships) == len(SHIP_SIZES)):
          self.state = PLAYER_TURN
      
      elif (self.state == PLAYER_TURN):
        self.player.update(self.state)
        self.player.moves[-1].append(hasShipConflict([self.player.moves[-1]], self.agent.ships))
        # if hits, add true to the last move

        self.board.draw_moves(self.player.moves)
        self.state = AI_TURN

      elif (self.state == AI_TURN):
        self.agent.update(self.player.ships)
        self.agent.moves[-1].append(hasShipConflict([self.agent.moves[-1]], self.player.ships))
        # if hits, add true to the last move

        self.board.draw_moves(self.agent.moves)
        self.state = PLAYER_TURN
      
      if (testWin(self.agent.moves)):
        print("\nIA venceu!")
        self.running = False
        break
      elif (testWin(self.player.moves)):
        print("\nJogador venceu!")
        self.running = False
        break
