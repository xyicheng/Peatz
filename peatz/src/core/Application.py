from core.Object import Object
import importlib as il

class Application(Object):

    STARTING_STATE = 'Main'
    
    def __init__(self):
        self.app_name = self.__class__.__name__
    
    def show(self, view):
        self.controller = getattr(il.import_module(self.app_name.lower() + '.controller.' + view + 'Controller'), view + 'Controller')(self);
        self.controller.render();
        
    def start(self):
        self.show(self.STARTING_STATE);