def hasShipConflict(positions, ships) -> bool:
  for pos in positions:
    for ship in ships:
      for ship_pos in ship.positions:
        if pos == ship_pos:
          return True

def testWin(moves) -> bool:
  hit_count = 0
  for move in moves:
    if (move[2]):
      hit_count += 1

  return hit_count == 17