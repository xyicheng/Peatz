from peatz.core.Object import Object
from peatz.core.ui.constructors.xml.XmlViewConstructor import XmlViewConstructor


class Controller(Object):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.view_constructor = XmlViewConstructor(self.app)
        self.view_name = self.__class__.__name__[:-10]

    def render(self):
        self.view_constructor.construct(self.view_name);
        self.view = self.view_constructor.view
        self.view.render()