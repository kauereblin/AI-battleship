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
  state = PLACING_SHIPS
  orientation = False

  def __init__(self) -> None:
    pygame.init()
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Battleship Board")

  def run(self) -> None:
    while self.running:
      self.update()
      self.draw()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
          break

        if (self.state == PLACING_SHIPS):
          if (event.type == pygame.MOUSEMOTION):
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = (mouse_pos[0] // CELL_WIDTH) * CELL_WIDTH
            mouse_y = (mouse_pos[1] // CELL_HEIGHT) * CELL_HEIGHT

            positions = []
            idx_size = len(self.player.ships)
            size = SHIP_SIZES[idx_size]
            rec = None
            for pos in range(1, size + 1):
              if (self.orientation):
                rec = pygame.Rect(mouse_x, mouse_y // CELL_HEIGHT * pos, CELL_WIDTH, CELL_HEIGHT)
              else:
                rec = pygame.Rect(mouse_x // CELL_WIDTH * pos, mouse_y, CELL_WIDTH, CELL_HEIGHT)

              pygame.draw.rect(self.board.surface, pygame.Color(66, 66, 66, 60), rec)
              positions.append([mouse_x // CELL_WIDTH, mouse_y // CELL_HEIGHT])

              idx_size -= 1

          if event.type == pygame.MOUSEBUTTONDOWN: # place ship
            if event.button == 1:
              self.player.add_ship(positions, self.orientation)
              if len(self.player.ships) == len(SHIP_SIZES):
                self.state = PLAYER_TURN

          if event.type == pygame.KEYDOWN: # rotate ship
            if event.key == pygame.K_o:
              self.orientation = not self.orientation

            if event.key == pygame.K_SPACE: # end placing ships
              self.state = PLAYER_TURN

    pygame.quit()

  def update(self) -> None:
    self.player.update()
    self.agent.update()
    self.board.update()

  def draw(self) -> None:
    self.agent .draw(self.board.surface)
    self.player.draw(self.board.surface)
    self.board .draw()
    self.screen.blit(self.board.surface, (SCREEN_WIDTH // 2 - BOARD_WIDTH // 2, SCREEN_HEIGHT // 2 - BOARD_HEIGHT // 2))
    pygame.display.flip()
