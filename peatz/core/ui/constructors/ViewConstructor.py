from tkinter import *

from peatz.core.Object import Object
from peatz.core.ui.View import View


class ViewConstructor(Object):

    def __init__(self, app):
        self.view = View()
        self.view.root = app.root
        self.app = app

    def construct(self, view_name):
        pass
