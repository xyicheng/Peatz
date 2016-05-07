from peatz.core.Object import Object
from peatz.core import constants
import settings, sys, os, importlib as il

class Peatz(Object):
            
    def start_app(self, app_name):
        mod = il.import_module(app_name.lower() + '.' + app_name);
        app = getattr(mod, app_name)()
        app.start()
        
peatz = Peatz();
peatz.start_app('MyApp')