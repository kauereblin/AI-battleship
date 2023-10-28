# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BOARD_WIDTH = 500
BOARD_HEIGHT = 500

GRID_SIZE = 10

CELL_WIDTH = BOARD_WIDTH // GRID_SIZE
CELL_HEIGHT = BOARD_HEIGHT // GRID_SIZE

# Cell states
NOT_PLAYED = 0
WATER = 1
SHIP = 2

# Game states
PLACING_SHIPS = 0
PLAYER_TURN = 1
AI_TURN = 2

SHIP_SIZES = [5, 4, 3, 3, 2]