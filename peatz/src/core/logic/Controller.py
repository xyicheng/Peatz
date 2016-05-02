from core.Object import Object
from core.ui.constructors.xml.XmlViewConstructor import XmlViewConstructor

class Controller(Object):
    
    def __init__(self):
        super().__init__()
        self.view_constructor = XmlViewConstructor()
        self.view_name = self.__class__.__name__[:-10]
        
    def render(self):
        self.view = self.view_constructor.construct(self.view_name);
        self.view.render()