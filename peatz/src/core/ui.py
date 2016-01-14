from core.core import Object
from core.data import *

class UIElement(Object):
    width=50
    height=50

class View(UIElement):
    
    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.binding = Binding(dict())
        self.UIElements = UIElementCollection(dict())
        self.layout = Layout()
        
    def render(self):
        pass
        #self.frame.mainloop()

class Layout(UIElement):
    pass
    
class Control(UIElement):
    pass
    
class UserControl(Control):
    pass