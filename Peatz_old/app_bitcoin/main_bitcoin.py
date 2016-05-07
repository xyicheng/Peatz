# THIS FILE HAS BEEN GENERATED AUTOMATICALY
# Bitcoin MAIN FILE
# DO NOT DELETE OR RENAME THIS FILE & THE __INIT__ METHOD

from peatz.core.core import Application

class BitcoinApplication(Application):
	
	def __init__(self):
		super().__init__('Bitcoin')
		# INIT YOUR APPLICATION HERE
		self.start()
		
	def start(self):
		super().start()
		# FIRST METHOD CALLED ON STARTING