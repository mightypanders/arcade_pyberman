from states import *
from stateController import StateControl

frames = 60

app = StateControl(frames)
state_dict = {
	'menu': Menu(),
	'game': Game()
}
app.setup_states(state_dict, 'menu')
app.main_game_loop()
