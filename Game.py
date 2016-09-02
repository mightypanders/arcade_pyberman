from states import States
import arcade


class Game(States):
	def __init__(self):
		States.__init__(self)
		self.next= "menu"
		self.all_sprites = arcade.SpriteList()
		self.wall_list = arcade.SpriteList()

		self.countHorBlock = 8
		self.countVertBlock = 10




