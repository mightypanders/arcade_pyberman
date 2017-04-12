import arcade
import glob

class BaseState(arcade.Window):
	def __init__(self):
		super().__init__(glob.SCR_W,glob.SCR_H,"pyberman")
		self.done = False
		self.next = None
		self.quit = False
		self.prev = None

	def cleanup(self):
		pass

	def startup(self):
		pass

	def on_key_press(self, symbol: int, modifiers: int):
		pass

	def on_key_release(self, symbol: int, modifiers: int):
		pass

	def update(self):
		pass

	def on_draw(self):
		pass

	def handle_events(self,event):
		pass

