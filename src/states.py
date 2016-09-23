import arcade
from const import *

class States(arcade.Window):
	def __init__(self):
		super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,TITLE)
		self.done = False
		self.next = None
		self.quit = False
		self.prev = None
		arcade.start_render()
	def cleanup(self):
		pass
	def startup(self):
		pass
	def handle_events(self, event):
		pass
	def update(self):
		pass
	def on_draw(self):
		pass


class Menu(States):
	def __init__(self):
		States.__init__(self)
		self.next = "game"
		self.menu_items = ("Start", "Options", "Quit")
		print("menu state initialized")

	def cleanup(self):
		self.labels = None

	def startup(self):
		self.labels = []

	def handle_events(self, event):
		pass

	def update(self):
		self.on_draw()

	def on_draw(self):
		pass


class Game(States):
	def __init__(self):
		States.__init__(self)
		self.next = "menu"
		self.all_sprites = arcade.SpriteList()
		self.wall_list = arcade.SpriteList()

		self.countHorBlock = 8
		self.countVertBlock = 10
		print("gamestate initialized")
