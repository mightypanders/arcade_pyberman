import  arcade
from const import *
from entity import *

class SpritePlayer(arcade.AnimatedWalkingSprite):
	def __init__(self, scale, playernumber, color):
		super().__init__(scale=scale)
		self.PlayerNo = playernumber
		self.color = color
		self.bomb_list = arcade.SpriteList()
		self.assingTextures()
		self.walkleftkey = arcade.key.LEFT
		self.walkrightkey = arcade.key.RIGHT
		self.walkupkey = arcade.key.UP
		self.walkdownkey = arcade.key.DOWN
		self.bombkey = arcade.key.SPACE

		self.texture_change_distance = 50
		self.center_y =  SCREEN_HEIGHT/ 2
		self.center_x = SCREEN_WIDTH / 2

	def putbomb(self):
		bomb = SpriteBomb(self)
		self.bomb_list.append(bomb)

	def getKeyDownEvent(self, key):
		if key == self.walkupkey:
			self.change_y += DEFAULT_MOVE_SPEED
		elif key == self.walkdownkey:
			self.change_y -= DEFAULT_MOVE_SPEED
		elif key == self.walkleftkey:
			self.change_x -= DEFAULT_MOVE_SPEED
		elif key == self.walkrightkey:
			self.change_x += DEFAULT_MOVE_SPEED
		elif key == self.bombkey:
			self.putbomb()

	def getKeyUpEvent(self, key):
		if key == self.walkupkey:
			self.change_y -= DEFAULT_MOVE_SPEED
		elif key == self.walkdownkey:
			self.change_y += DEFAULT_MOVE_SPEED
		elif key == self.walkleftkey:
			self.change_x += DEFAULT_MOVE_SPEED
		elif key == self.walkrightkey:
			self.change_x -= DEFAULT_MOVE_SPEED

	def assingTextures(self):
		file = "images/SBM2-Bomberman.gif"

		stand_left_right = [[52, 00, 16, 28]]
		self.stand_right_textures = arcade.load_textures(file, stand_left_right, False)
		self.stand_left_textures = arcade.load_textures(file, stand_left_right, True)

		stand_up = [[00, 00, 18, 28]]
		self.stand_up_textures = arcade.load_textures(file, stand_up, False)

		stand_down = [[105, 00, 18, 28]]
		self.stand_down_textures = arcade.load_textures(file, stand_down, False)

		walk_sprites = [[52, 00, 16, 28],
		                [72, 00, 16, 28],
		                [52, 00, 16, 28],
		                [89, 00, 16, 28]]
		self.walk_right_textures = \
			arcade.load_textures(file, walk_sprites, False)
		self.walk_left_textures = \
			arcade.load_textures(file, walk_sprites, True)

		walk_sprites = [[00, 00, 18, 28],
		                [18, 00, 18, 28],
		                [00, 00, 18, 28],
		                [36, 00, 18, 28]]
		self.walk_up_walk_textures = arcade.load_textures(file, walk_sprites, False)

		walk_sprites = [[105, 00, 18, 28],
		                [123, 00, 18, 28],
		                [105, 00, 18, 28],
		                [141, 00, 18, 28]]
		self.walk_down_textures = arcade.load_textures(file, walk_sprites, False)
