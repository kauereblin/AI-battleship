import random
from time import sleep
from Ship import Ship
from constants import *
from util import *

class Agent:
    ships = []
    moves = []
    targets = []
    last_hit = None
    hit_orientation = None
    hit_directions = ['up', 'down', 'left', 'right']

    def __init__(self) -> None:
        self.set_ships()

    def set_ships(self) -> None:
        idx = len(SHIP_SIZES) - 1
        while idx >= 0:
            # for each ship size
            size = SHIP_SIZES[idx]
            orientation = random.randint(0, 1)

            positions = []
            if orientation == 0:  # horizontal
                x = random.randint(0, GRID_SIZE - size)
                y = random.randint(0, GRID_SIZE - 1)
                positions = [[x + _, y] for _ in range(size)]
            else:  # vertical
                x = random.randint(0, GRID_SIZE - 1)
                y = random.randint(0, GRID_SIZE - size)
                positions = [[x, y + _] for _ in range(size)]

            if hasShipConflict(positions, self.ships):
                # if there is a conflict, try to generate another position for the ship
                continue

            new_ship = Ship(positions, size, orientation)
            self.ships.append(new_ship)
            idx -= 1

    def guess_random(self):
        while True:
            # generate a random position to shoot
            guess_row, guess_col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
            if [guess_row, guess_col, True | False] not in self.moves:
                break

        return [guess_row, guess_col]

    def update(self, player_ships) -> None:
        if not self.targets:
            guess_row, guess_col = self.guess_random()
        else:
            guess_row, guess_col = self.targets.pop()

        hit_result = hasShipConflict([[guess_row, guess_col]], player_ships)

        if hit_result:
            if self.last_hit is None:
                # First hit, store the position and start searching for orientation
                self.last_hit = [guess_row, guess_col]
            else:
                # Subsequent hits, try to determine the orientation
                if self.hit_orientation is None:
                    if self.last_hit[0] == guess_row:
                        self.hit_orientation = 'horizontal'
                        self.hit_directions = ['left', 'right']
                    elif self.last_hit[1] == guess_col:
                        self.hit_orientation = 'vertical'
                        self.hit_directions = ['up', 'down']
                    else:
                        # Guessed the direction wrong, revert to random firing
                        self.hit_orientation = None
                        self.hit_directions = ['up', 'down', 'left', 'right']
                        self.targets.clear()
                        self.last_hit = None
                        return self.update(player_ships)

                # Add adjacent positions to targets
                self.add_adjacent_targets(guess_row, guess_col)

        self.moves.append([guess_row, guess_col, hit_result])

    def add_adjacent_targets(self, row, col):
        if self.hit_orientation == 'horizontal':
            potential_targets = [[row, col + 1], [row, col - 1]]
        elif self.hit_orientation == 'vertical':
            potential_targets = [[row + 1, col], [row - 1, col]]
        else:
            potential_targets = []

        for move_x, move_y in potential_targets:
            if (
                0 <= move_x < GRID_SIZE
                and 0 <= move_y < GRID_SIZE
                and [move_x, move_y, True | False] not in self.moves
                and [move_x, move_y] not in self.targets
            ):
                self.targets.append([move_x, move_y])