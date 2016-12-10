import arcade
from const import *

class GameState():
	def __init__(self):
		self.done=False
		self.next=None
		self.quit=False
		self.prev=None

class Menu(GameState):
	def __init__(self):
		super().__init__()
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


class Game(GameState):
	def __init__(self):
		super().__init__()
		self.next = "menu"
		self.all_sprites = arcade.SpriteList()
		self.wall_list = arcade.SpriteList()

		self.countHorBlock = 8
		self.countVertBlock = 10
		print("gamestate initialized")

