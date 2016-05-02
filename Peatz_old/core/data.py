import threading

from core.core import Object, Application
from core.exception import *
        
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
        
