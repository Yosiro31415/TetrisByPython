from pygame.locals import *
import pygame
import sys
import math as ma


class InputManager:
    def __init__(self, gManager):
        self.gManager = gManager

    def main(self):
        listKey = []
        if pygame.key.get_focused():
            if pygame.key.get_pressed()[K_w]:
                listKey.append("w")
            if pygame.key.get_pressed()[K_a]:
                listKey.append("a")
            if pygame.key.get_pressed()[K_s]:
                listKey.append("s")
            if pygame.key.get_pressed()[K_d]:
                listKey.append("d")
            if pygame.key.get_pressed()[K_q]:
                listKey.append("q")
            if pygame.key.get_pressed()[K_e]:
                listKey.append("e")
        return listKey


class DrowingManager:
    def __init__(self, gManager):
        self.flame = 0
        self.gManager = gManager
        self.screen = pygame.display.set_mode((100, 100))
        pygame.display.set_caption("tetris")
        self.oldTime = pygame.time.get_ticks

    def updateDisplay(self):
        pygame.display.update()
        return True

    def main(self):
        self.flame += 1
        print(self.flame)
        self.screen.fill(
            (abs(256. * ma.sin(self.flame / 1000. + 0 * ma.pi / 3.)),
             abs(256. * ma.sin(self.flame / 1000. + 1 * ma.pi / 3.)),
             abs(256. * ma.sin(self.flame / 1000. + 2 * ma.pi / 3.))))
        self.updateDisplay()
        return True


class GameManager:

    def __init__(self):
        pygame.init()
        self.dManager = DrowingManager(self)
        self.iManager = InputManager(self)
        self.isRunning = True
        self.listKey = []
        self.instClock = pygame.time.Clock()
        return


    def getKeyList(self):
        self.listKey = self.iManager.main()

    def testMove(self):
        pygame.event.pump()  # おまじない(空のイベントを呼び出して，更新してるらしい)
        print(self.listKey)
        if "w" in self.listKey:
            pass
        if "a" in self.listKey:
            pass
        if "s" in self.listKey:
            pass
        if "d" in self.listKey:
            pass
        if "q" in self.listKey:
            self.isRunning = False
        return True

    def mainLoop(self):
        self.instClock.tick_busy_loop(60)
        print(self.instClock.get_fps())
        self.iManager.main()
        if self.isRunning:
            self.getKeyList()
            self.testMove()
            self.dManager.main()
            return True
        else:
            return False
