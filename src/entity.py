import datetime

import arcade


class Player(arcade.AnimatedWalkingSprite):
	def __init__(self, playerno, color, filename):
		super().__init__()
		self.playernumber = playerno
		self.stand_right_textures = None
		self.bomb_list = []

	def put_bomb(self):
		bomb = Bomb(self, datetime.time)
		self.bomb_list.append(bomb)


class Wall():
	def __init__(self):
		self.color = 2


class Bomb(arcade.AnimatedTimeSprite):
	def __init__(self, player, placed):
		super().__init__()
		self.player = player
		self.timeplaced = placed
		self.init_textures()

	def init_textures(self):
		file = "images/14bomberman.PNG"
		loc = [[50, 255, 16, 17],
		       [33, 255, 16, 17],
		       [18, 255, 16, 17],
		       [33, 255, 16, 17], ]
		self.textures = arcade.load_textures(file, loc, False)
