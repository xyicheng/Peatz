from core.core import Object
from core.ui import View

class ViewController(Object):
    
    def __init__(self, view):
        super().__init__(self.__class__.__name__)
        self.view = view
        
    def render(self):
        self.view.render()
        
    def set(self, key, value=None):
        self.view.binding.set(key, value)
        
    def get(self, key):
        self.view.UIElements.get(key)
        
    def before(self):
        pass;
        
    def after(self):
        pass;