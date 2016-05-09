from tkinter import *

from peatz.core.Object import Object
from peatz.core.ui.View import View

class ViewConstructor(Object):

    def __init__(self, app):
        self.view = View()
        self.app = app;
        self.view.root = app.root;
        
        
    def construct(self, view_name):
        pass;