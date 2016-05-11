from tkinter import *

from peatz.core.Object import Object
from peatz.core.data.collections.UIElementCollection import UIElementCollection


class View(Object):

    def __init__(self):
        super().__init__()
        self.elements = UIElementCollection({});

    def render(self):
        pass;
        #self.root.mainloop()
        
    def add(self, element):
        self.elements.add(element);