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

	def on_key_press(self, symbol: int, modifiers: int):
		super().on_key_press(symbol,modifiers)
		print("press")

	def on_key_release(self, symbol: int, modifiers: int):
		super().on_key_release(symbol,modifiers)
		print("release")

	def update(self):
		self.on_draw()

	def on_draw(self):
		pass

	def handle_events(self,event):
		pass

