from pygame.locals import *
import pygame
import sys
import math as ma
from Enum import enum


class KEY(enum):
    q = 0
    w = 1
    e = 2
    a = 3
    s = 4
    d = 5

class InputManager:
    gManager = 0

    def __init__(self, gManager):
        self.gManager = gManager
        pygame.key.set_repeat(delay, 100)

    def main(self):
        listKey = []
        if pygame.key.get_focused():
            if pygame.key.get_pressed()["w"]:
                listKey.append("w")
            if pygame.key.get_pressed()["a"]:
                listKey.append("a")
            if pygame.key.get_pressed()["s"]:
                listKey.append("s")
            if pygame.key.get_pressed()["d"]:
                listKey.append("d")
        return listKey


class DrowingManager:
    gManager = 0

    def __init__(self, gManager):
        self.gManager = gManager
        pass

    def main(self):
        self.screen.fill(
            (abs(256. * ma.sin(self.time + 0 * ma.pi / 3.)),
             abs(256. * ma.sin(self.time + 1 * ma.pi / 3.)),
             abs(256. * ma.sin(self.time + 2 * ma.pi / 3.))))


class GameManager:
    isRunning = False
    screen = 0
    time = 0
    DManager = DrowingManager(self)
    IManager = InputManager(self)
    listKey = []
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((3000, 2000))
        pygame.display.set_caption("tetris")
        self.isRunning = True
        return
    def testMove(self):
        pass
    def mainLoop(self):
        listKey = Imanager
        if self.isRunning:
            self.time += 0.005
            self.DManager.DrowingMain()
            pygame.display.update()
            return True
        else:
            return False
