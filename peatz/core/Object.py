class Object(object):

    def __init__(self):
        self.name = self.__class__.__name__

    def __str__(self):
        return self.name
