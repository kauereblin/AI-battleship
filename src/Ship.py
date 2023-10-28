class Ship:
  def __init__(self, positions, size, orientation):
    self.positions = {'x': [pos[0] for pos in positions], 'y': [pos[1] for pos in positions]}
    self.size = size
    self.orientation = orientation
    self.hit = [False] * size

  def draw(self, surface):
    pass

  def is_hit(self, x, y):
    pass
