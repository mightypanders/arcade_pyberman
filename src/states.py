import arcade

class States:
	def __init__(self):
		self.done = False
		self.next = None
		self.quit = False
		self.prev = None
		self.screen = None


class Menu(States):
	def __init__(self):
		States.__init__(self)
		self.next = "game"
		self.menu_items = ("Start", "Options", "Quit")

	def cleanup(self):
		self.labels = None

	def startup(self):
		self.labels = []

	def get_event(self, event):
		if event == None:
			self.done, self.quit = True, True

	def update(self, screen, dt):
		self.draw()

	def draw(self):
		print("success")


class Game(States):
	def __init__(self):
		States.__init__(self)
		self.next = "menu"
		self.all_sprites = arcade.SpriteList()
		self.wall_list = arcade.SpriteList()

		self.countHorBlock = 8
		self.countVertBlock = 10


