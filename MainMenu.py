from states import States

class Menu(States):
	def __init__(self):
		States.__init__(self)
		self.next = "game"
		self.menu_items=("Start","Options","Quit")

	def cleanup(self):
		self.labels = None

	def startup(self):
		self.labels=[]

	def get_event(self,event):
		if event.type == None:
			self.done, self.quit = True,True

	def update(self,screen,dt):
		self.draw(screen)
	def draw(self,screen):
		screen.fill()
