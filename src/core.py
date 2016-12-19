import arcade
from BaseState import *
from const import *

class GameWindow(arcade.Window):
	def __init__(self):
		super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT)
		self.current_state,self.previous_state=self.state_selector(enStateDict.default)

	def state_selector(self,GameState):
		if GameState == enStateDict.default:
			pass
		elif GameState == enStateDict.game:
			pass
		elif GameState == enStateDict.menu:
			menu = Menu()
			return menu
		elif GameState == enStateDict.options:
			pass
		elif GameState == enStateDict.scoreboard:
			pass
		elif GameState == enStateDict.gameover:
			pass
		elif GameState == enStateDict.gameprep:
			pass

	def on_draw(self):
		arcade.start_render()
		self.state.on_draw()

	def animate(self,dt):
		pass

