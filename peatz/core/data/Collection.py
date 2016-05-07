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