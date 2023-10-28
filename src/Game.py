import pygame

from Agent import Agent
from Player import Player
from Board import Board

from constants import *

class Game:
  running = True
  screen = None
  board = Board()
  agent = Agent()
  player = Player()

  def __init__(self) -> None:
    pygame.init()
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Battleship Board")
    self.agent = Agent()

  def run(self) -> None:
    while self.running:
      self.update()
      self.draw()
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False

    pygame.quit()

  def update(self) -> None:
    self.board.update()
    self.agent.update()
    self.player.update()

  def draw(self) -> None:
    self.board.draw()
    self.agent.draw()
    self.player.draw()
    self.screen.blit(self.board.board_surface, (SCREEN_WIDTH // 2 - BOARD_WIDTH // 2, SCREEN_HEIGHT // 2 - BOARD_HEIGHT // 2))
    pygame.display.flip()
