class Ship:
  def __init__(self, positions, size, orientation):
    self.positions = positions
    self.size = size
    self.orientation = orientation
    self.hit = [False] * size
