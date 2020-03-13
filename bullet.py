'''
the class of bullet
'''
from config import *


class BaseBullet(object):
    sum = 0
    attack = 10
    speed = 15
    load_time = 100
    path_set = {'right': None,
                'left': None,
                'forward': None,
                'backward': None}

    def __init__(self, direction='right', site=(0, 0)):
        self.direction = direction
        self.path = BaseBullet.path_set[self.direction]
        self.exist = True
        self.site = site
        self.size = (10, 10)
        BaseBullet.sum += 1

    def move(self):
        if self.direction == 'left':
            self.site = (self.site[X] - self.speed, self.site[Y])
        elif self.direction == 'right':
            self.site = (self.site[X] + self.speed, self.site[Y])
        elif self.direction == 'backward':
            self.site = (self.site[X], self.site[Y] + self.speed)
        elif self.direction == 'forward':
            self.site = (self.site[X], self.site[Y] - self.speed)
        else:
            pass


class PlayerBullet(BaseBullet):
    attack = 20
    speed = 20
    load_time = 50
    set = []
    path_set = {'right': None,
                'left': None,
                'forward': None,
                'backward': None}

    def __init__(self, direction='right', site=(0, 0)):
        BaseBullet.__init__(self, direction=direction, site=site)
        self.set.append(self)


class EnemyBullet(BaseBullet):
    attack = 10
    speed = 15
    load_time = 100
    set = []
    path_set = {'right': None,
                'left': None,
                'forward': None,
                'backward': None}

    def __init__(self, direction='right', site=(0, 0)):
        BaseBullet.__init__(self, direction=direction, site=site)
        self.set.append(self)
