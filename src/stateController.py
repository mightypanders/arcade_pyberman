class StateControl:
	def __init__(self, fps):
		self.fps = fps
		self.done = False
		self.screen = None
		self.clock = None
		self.state = None

	def setup_states(self, state_dict, start_state):
		self.state_dict = state_dict
		self.state_name = start_state
		self.state = self.state_dict[self.state_name]
		self.state.startup()

	def flip_state(self):
		self.state_done = False
		prev, self.state_name = self.state_name, self.state.next
		self.state.cleanup()
		self.state = self.state_dict[self.state_name]
		self.state.startup()
		self.state.prev = prev

	def update(self):
		if self.state.quit:
			self.done = True
		elif self.state.done:
			self.flip_state()
		self.state.update()

	def event_loop(self):
		# get events here
		# self.state.handle_events()
		pass

	def main_game_loop(self):
		while not self.done:
			self.event_loop()
			self.update()
		# update display
