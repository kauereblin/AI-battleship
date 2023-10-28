import pygame

class Ship:
  def __init__(self, x, y, length, orientation):
    self.x = x
    self.y = y
    self.length = length
    self.orientation = orientation
    self.hit = [False] * length

  def draw(self, surface):
    pass

  def is_hit(self, x, y):
    pass

class Carrier(Ship):
  def __init__(self, x, y, orientation):
    super().__init__(x, y, 5, orientation)

  def draw(self, surface):
    pass

class Battleship(Ship):
  def __init__(self, x, y, orientation):
    super().__init__(x, y, 4, orientation)

  def draw(self, surface):
    pass

class Cruiser(Ship):
  def __init__(self, x, y, orientation):
    super().__init__(x, y, 3, orientation)

  def draw(self, surface):
    pass

class Submarine(Ship):
  def __init__(self, x, y, orientation):
    super().__init__(x, y, 3, orientation)

  def draw(self, surface):
    pass

class Destroyer(Ship):
  def __init__(self, x, y, orientation):
    super().__init__(x, y, 2, orientation)

  def draw(self, surface):
    pass
