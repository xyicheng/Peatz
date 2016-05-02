from core.Application import Application

class MyApp(Application):
    
    STARTING_VIEW = 'MainView'
    
    def __init__(self):
        super().__init__();