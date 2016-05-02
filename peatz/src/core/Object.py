class Object(object):

    def __init__(self, name=None):
        if name is None:
            self.name = 'Default' + self.__class__.__name__ + 'Name';
        else:
            self.name = name
            
    def debug(self, val):
        print('From ' + self.name + ': ' + val)