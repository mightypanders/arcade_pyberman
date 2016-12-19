import arcade


class GameState():
	def __init__(self):
		self.done = False
		self.next = None
		self.quit = False
		self.prev = None

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
