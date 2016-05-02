class ThreadCollection(Collection):
    
    def add(self, app):
        if type(app) is threading.Thread:
            self.set(app.name, app)
            return self
        else:
            raise ThreadCollectionException('Adding \'' + type(app).__name__ + '\' instead of Thread')
            
    def start(self, app_name):
        self.get(app_name).start()