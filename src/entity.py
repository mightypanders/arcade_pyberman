from datetime import datetime

import arcade

import texturestore


def init_textures():
	texturestore.bomb_sprite = get_bomb_textures()


def get_bomb_textures():
	#  TODO Bomb Background 192,192,192 Make transparent
	file = "images/14bomberman.PNG"
	loc = [[50, 255, 16, 17],
	       [33, 255, 16, 17],
	       [18, 255, 16, 17],
	       [33, 255, 16, 17]]
	return arcade.load_textures(file, loc, False)


class Wall():
	def __init__(self):
		self.color = 2


class SpriteBomb(arcade.AnimatedTimeSprite):
	def __init__(self, player):
		super().__init__()
		self.player = player
		self.timeplaced = datetime.now()
		self.textures = texturestore.bomb_sprite
		self.transparent = True
		self.set_position(player.center_x, player.center_y)
		self.texture_change_frames = 30

	def update(self):
		super(SpriteBomb, self).update()
		if datetime.now().second - self.timeplaced.second >= 3:
			self.kill()
