from peatz.core.logic import ViewController

class MainViewController(ViewController):
	
	def before(self):
		super().before()
		print('Before rendering')
		