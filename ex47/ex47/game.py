class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.list = [0, 1, 2]

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

    def listy(self, thing):
        self.list.append(thing)
        if thing >= 0:
            return self.list[min(1, thing)]
        else:
            return self.list[2]
