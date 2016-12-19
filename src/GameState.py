from BaseState import *

class Game(BaseState):
	def __init__(self):
		super().__init__()
		self.next = "menu"
		self.all_sprites = arcade.SpriteList()
		self.wall_list = arcade.SpriteList()

		self.countHorBlock = 8
		self.countVertBlock = 10
		print("gamestate initialized")

	def startup(self):
		pass  # TODO Fenster hier starten

	def cleanup(self):
		pass  # TODO Fenster hier in menü wechseln

	def handle_events(self, event):
		if type(event) == type(arcade.key):
			pass
		pass

	def update(self):
		pass

	def on_draw(self):
		pass
