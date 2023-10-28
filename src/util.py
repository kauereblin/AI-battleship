def hasShipConflict(positions, ships):
  for pos in positions:
    for ship in ships:
      for x, y in zip(ship.positions["x"], ship.positions["y"]):
        if pos == [x, y]:
          return True