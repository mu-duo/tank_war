import bullet, tank, world_monitor
import pygame
import world_monitor
from config import *
from _my_module import monitor


def main():
    t = tank.PlayerTank()
    m = world_monitor.Monitor(player_tank=t.set)
    m.run()
    mon = monitor.Monitor()
    mon.add(t)
    mon.start()
    while not GAME_OVER:
        t.key_in()
        t.load_bullet()
        pygame.time.delay(int(1000/FPS))


if __name__ == '__main__':
    main()