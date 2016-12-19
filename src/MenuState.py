from BaseState import *

class Menu(BaseState):
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

