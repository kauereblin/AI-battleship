def hasShipConflict(positions, ships) -> bool:
  for pos in positions:
    for ship in ships:
      for ship_pos in ship.positions:
        if pos[0] == ship_pos[0] and pos[1] == ship_pos[1]:
          return True
  return False

def testWin(moves) -> bool:
  hit_count = 0
  for move in moves:
    if (move[2]):
      hit_count += 1

  return hit_count == 17