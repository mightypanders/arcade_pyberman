import arcade


class BaseState():
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



