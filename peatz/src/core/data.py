import threading

from core.core import Object, Application
from core.exception import *

class Collection(Object):
    
    def __init__(self, items):
        if not type(items) is None:
            if type(items) is type(dict()):
                self.items = items;
            else:
                raise CollectionException('Setting items as \'' + type(items).__name__ + '\' instead of dictionary')
        
    def __len__(self):
        return self.length()
    
    def __str__(self):
        return str(self.items)
        
    def length(self):
        return len(self.items)
    
    def get(self, key):
        return self.items[key]
    
    def set(self, key, value=None):
        if not value is None:
            self.items[key] = value
        else:
            self.items.append(key)
       
class ThreadCollection(Collection):
    
    def add(self, app):
        if type(app) is threading.Thread:
            self.set(app.name, app)
            return self
        else:
            raise ThreadCollectionException('Adding \'' + type(app).__name__ + '\' instead of Thread')
            
    def start(self, app_name):
        self.get(app_name).start()
        
class ViewControllerCollection(Collection):
    
    last = None;
    
    def add(self, vc):
        from core.logic import ViewController
        if ViewController in type(vc).__bases__:
            self.last = vc
            self.set(vc.name, vc)
            return self
        else:
            raise ViewControllerCollectionException('Adding \'' + type(vc).__name__ + '\' instead of ViewController')
    
class Binding(Collection):
    
    def echo(self, key):
        print(self.get(key))
        
class UIElementCollection(Collection):
    pass