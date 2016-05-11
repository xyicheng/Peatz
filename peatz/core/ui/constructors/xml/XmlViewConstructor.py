import os
import xml.etree.ElementTree as ET
import tkinter
from peatz.core.ui.constructors.ViewConstructor import ViewConstructor
from peatz.core.ui.View import View
from peatz.core.constants import *

class XmlViewConstructor(ViewConstructor):

    def __init__(self, root):
        super().__init__(root);
        
    def construct(self, view_name):
        super().construct(view_name);
        self.tree = ET.parse(os.path.join(PROJECT_DIR, self.app.app_name, 'view', view_name + 'View.xml'))
        for child in self.tree.getroot():
            self.create(child)
            
    def create(self, element):
        self.view.add(getattr(tkinter,element.tag));
        
    def has_children(self, element):
        return True