import threading
from config import *
import pygame


class Monitor(object):
    def __init__(self, **kwarg):
        self.thread = threading.Thread(target=self.fun, args=(kwarg,))

    def run(self):
        self.thread.start()

    @staticmethod
    def reset(obj):
        obj.right = True
        obj.left = True
        obj.backward = True
        obj.forward = True

    @staticmethod
    def check_movable(obj):
        if obj.site[X] >= SCREEN_SIZE[X] - obj.size[X]:
            obj.right = False
        if obj.site[X] <= 0:
            obj.left = False
        if obj.site[Y] >= SCREEN_SIZE[Y] - obj.size[Y]:
            obj.backward = False
        if obj.site[Y] <= 0:
            obj.forward = False

    @staticmethod
    def object_check_hit(object_1, object_2):
        pass
        pass

    @staticmethod
    def set_check_hit(tank_set, bullet_set):
        for tank in tank_set:
            for bullet in bullet_set:
                if Monitor.object_check_hit(tank, bullet):
                    tank.get_hurt()
                    bullet.exist = False

    @staticmethod
    def fun(object_set):
        while not GAME_OVER:
            # if HURT_TEAMMATE:
            #     Monitor.set_check_hit(object_set['player_tank'], object_set['player_bullet'])
            # Monitor.set_check_hit(object_set['player_tank'], object_set['enemy_bullet'])
            # Monitor.set_check_hit(object_set['enemy_tank'], object_set['player_bullet'])
            Monitor.reset(object_set['player_tank'][0])
            Monitor.check_movable(object_set['player_tank'][0])

            pygame.time.delay(int(1000/FPS))
