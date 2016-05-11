from peatz.core.Object import Object


class Collection(Object):

    def __init__(self, items):
        if not type(items) is None:
            if isinstance(items, dict):
                self.items = items
            else:
                raise CollectionException(
                    'Setting items as \'' + type(items).__name__ + '\' instead of dictionary')

    def __len__(self):
        return self.length()

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return self.items.__iter__()

    def __getitem__(self, key):
        return self.items[key]

    def length(self):
        return len(self.items)

    def get(self, key):
        return self.items[key]

    def set(self, key, value=None):
        if value is not None:
            self.items[key] = value
        else:
            self.items.append(key)

    def add(self, element):
        self.set(self.length(), element)
