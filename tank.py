'''
the class of tank
'''
import bullet
import pygame
import random
from config import *


class BaseTank(object):
    speed = 5
    bullet = bullet.BaseBullet
    path_set = {
        'right': None,
        'left': None,
        'forward': None,
        'backward': None
    }

    def __init__(self, site=(0, 0), direction='right'):
        self.direction = direction
        self.path = self.path_set[self.direction]
        self.site = site
        self.bullet_load = 0
        self.hp = 100
        self.size = (100, 100)
        self.exist = True

        # judge the direction
        self.right = False
        self.left = False
        self.forward = False
        self.backward = False

    def enable_shoot(self):
        if self.bullet_load >= self.bullet.load_time:
            return True
        else:
            return False

    def shoot(self):
        self.bullet_load = 0
        return self.bullet(site=self.site)

    def load_bullet(self):
        if self.bullet_load < self.bullet.load_time:
            self.bullet_load += 1

    def turn_to_left(self):
        self.direction = 'left'
        self.path = EnemyTank.path_set[self.direction]

    def turn_to_right(self):
        self.direction = 'right'
        self.path = EnemyTank.path_set[self.direction]

    def turn_to_forward(self):
        self.direction = 'forward'
        self.path = EnemyTank.path_set[self.direction]

    def turn_to_backward(self):
        self.direction = 'backward'
        self.path = EnemyTank.path_set[self.direction]


class PlayerTank(BaseTank):
    speed = 5
    bullet = bullet.PlayerBullet
    set = []
    path_set = {
        'right': 'image/d.gif',
        'left': 'image/a.gif',
        'forward': 'image/w.gif',
        'backward': 'image/s.gif'
    }

    def __init__(self, site=(0, 0), direction='right'):
        BaseTank.__init__(self, site=site, direction=direction)
        self.life = 3
        self.set.append(self)

    def move_right(self):
        if self.right:
            self.site = (self.site[X] + self.speed, self.site[Y])

    def move_left(self):
        if self.left:
            self.site = (self.site[X] - self.speed, self.site[Y])

    def move_forward(self):
        if self.forward:
            self.site = (self.site[X], self.site[Y] - self.speed)

    def move_backward(self):
        if self.backward:
            self.site = (self.site[X], self.site[Y] + self.speed)

    def key_in(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.QUIT:
                    exit()

        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_ESCAPE]:
            exit()
        if key_list[pygame.K_w]:
            if self.direction != 'forward':
                self.direction = 'forward'
                self.path = self.path_set[self.direction]
            self.move_forward()
        elif key_list[pygame.K_s]:
            if self.direction != 'backward':
                self.direction = 'backward'
                self.path = self.path_set[self.direction]
            self.move_backward()
        elif key_list[pygame.K_d]:
            if self.direction != 'right':
                self.direction = 'right'
                self.path = self.path_set[self.direction]
            self.move_right()
        elif key_list[pygame.K_a]:
            if self.direction != 'left':
                self.direction = 'left'
                self.path = self.path_set[self.direction]
            self.move_left()
        if key_list[pygame.K_SPACE]:
            if self.enable_shoot():
                self.shoot()


class EnemyTank(BaseTank):
    speed = 5
    bullet = bullet.BaseBullet
    set = []
    path_set = {'right': None,
                'left': None,
                'forward': None,
                'backward': None}

    def __init__(self, site=(random.randint(0, 140)*5, random.randint(0, 140)*5), direction='right'):
        BaseTank.__init__(self, site=site, direction=direction)
        self.set.append(self)

    def move(self):
        if self.direction == 'left':
            if self.left:
                self.site = (self.site[X] - self.speed, self.site[Y])
        elif self.direction == 'right':
            if self.right:
                self.site = (self.site[X] + self.speed, self.site[Y])
        elif self.direction == 'backward':
            if self.backward:
                self.site = (self.site[X], self.site[Y] + self.speed)
        elif self.direction == 'forward':
            if self.forward:
                self.site = (self.site[X], self.site[Y] - self.speed)
        else:
            pass

    def watch(self):
        self.move()
