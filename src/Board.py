import pygame
from constants import *

class Board:
  board_surface = None
  
  def __init__(self) -> None:
    self.board_surface = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))
    self.board_surface.fill(WHITE)

  def update(self) -> None:
    pass

  def draw(self) -> None:
    for x in range(0, BOARD_WIDTH, CELL_WIDTH):
      pygame.draw.line(self.board_surface, BLACK, (x, 0), (x, BOARD_HEIGHT))
    for y in range(0, BOARD_HEIGHT, CELL_HEIGHT):
      pygame.draw.line(self.board_surface, BLACK, (0, y), (BOARD_WIDTH, y))

    font = pygame.font.SysFont(None, 24)
    for i in range(10):
      letter = font.render(chr(ord('A') + i), True, BLACK)
      number = font.render(str(i + 1), True, BLACK)
      self.board_surface.blit(letter, (i * CELL_WIDTH + CELL_WIDTH // 2 - letter.get_width() // 2, BOARD_HEIGHT - CELL_HEIGHT))
      self.board_surface.blit(number, (0, i * CELL_HEIGHT + CELL_HEIGHT // 2 - number.get_height() // 2))
