class Map(object):
    set = []
    life = 1
    size = (100, 100)
    path = None
    passable = False

    def __init__(self, site=(0 ,0)):
        self.exist = True
        self.site = site


class Wood(Map):
    life = 1
    path = 'image/map/wood.png'
    passable = False

    def __init__(self, site=(0, 0)):
        Map.__init__(self, site=site)
        self.set.append(self)


class Stone(Map):
    set = []
    life = 3
    path = 'image/map/stone.png'
    passable = False

    def __init__(self, site=(0, 0)):
        Map.__init__(self, site=site)
        self.set.append(self)


class Water(Map):
    set = []
    life = - 10
    path = 'image/map/water.png'
    passable = False

    def __init__(self, site=(0, 0)):
        Map.__init__(self, site=site)
        self.set.append(self)
        
        
class Iron(Map):
    set = []
    life = 3
    path = 'image/map/iron.png'
    passable = False

    def __init__(self, site=(0, 0)):
        Map.__init__(self, site=site)
        self.set.append(self)


