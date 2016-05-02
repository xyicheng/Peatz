from core.Object import Object
from core import constants
import settings, sys, os, importlib as il

class Peatz(Object):
    
    def __init__(self):
        self.load_apps();
        
    def load_apps(self):
        sys.path.append(constants.PROJECT_DIR)
        sys.path.append(constants.PROJECT_DIR + constants.DS + 'peatz' + constants.DS + 'src')
        for app in settings.APPLICATIONS :
            sys.path.append(os.path.join(constants.PROJECT_DIR, app.lower()))
            
    def start_app(self, app_name):
        mod = il.import_module(app_name);
        app = getattr(mod, app_name)()
        app.start()
        
peatz = Peatz();
peatz.start_app('MyApp')