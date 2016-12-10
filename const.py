from enum import Enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "pyberman"
DEFAULT_MOVE_SPEED = 3


class enStateDict(Enum):
	default = 0
	game = 1
	options = 2
	menu = 3
	gameprep = 4
	gameover = 5
	scoreboard = 6
