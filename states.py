from Game import Game
from MainMenu import Menu


class States(object):
	def __init__(self):
		self.done = False
		self.next = None
		self.quit = False
		self.prev = None
		self.screen = None


class StateControl:
	def __init__(self, fps):
		self.fps = fps
		self.done = False
		self.screen = None
		self.clock = None

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

	def update(self, dt):
		if self.state.quit:
			self.done = True
		elif self.state.done:
			self.flip_state()
		self.state.update(self.screen, dt)

	def event_loop(self):
		# get events here
		self.state.get_event()

	def main_game_loop(self):
		while not self.done:
			delta_time = self.clock.tick(self.fps) / 1000.0
			self.event_loop()
			self.update(delta_time)
		# update display


fps = 60

app = StateControl(fps)
state_dict = {
	'menu': Menu(),
	'game': Game()
}
app.setup_states(state_dict, 'menu')
app.main_game_loop()
