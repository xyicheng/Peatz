from core.ui.constructors.ViewConstructor import ViewConstructor
from core.ui.View import View

class XmlViewConstructor(ViewConstructor):
    
    def construct(self, view_name):
        return View()