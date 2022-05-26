from pygame.locals import *
import pygame
import sys
import math as ma


class InputManager:
    gManager = 0

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
    gManager = 0
    screen = 0
    time = 0.

    def __init__(self, gManager):
        self.gManager = gManager
        self.screen = pygame.display.set_mode((100, 100))
        pygame.display.set_caption("tetris")

    def updateDisplay(self):
        pygame.display.update()

    def main(self):
        self.time += 0.001
        print(self.time)
        self.screen.fill(
            (abs(256. * ma.sin(self.time + 0 * ma.pi / 3.)),
             abs(256. * ma.sin(self.time + 1 * ma.pi / 3.)),
             abs(256. * ma.sin(self.time + 2 * ma.pi / 3.))))
        self.updateDisplay()


class GameManager:
    isRunning = False
    dManager = 0
    iManager = 0
    listKey = []
    
    def __init__(self):
        pygame.init()
        self.dManager = DrowingManager(self)
        self.iManager = InputManager(self)
        self.isRunning = True
        return

    def getKeyList(self):
        self.listKey = self.iManager.main()

    def testMove(self):
        pygame.event.pump()  # おまじない(空のイベントを呼び出して，更新してるらしい)
        print(self.listKey)
        if "w" in self.listKey:
            print("w")
        if "a" in self.listKey:
            print("a")
        if "s" in self.listKey:
            print("s")
        if "d" in self.listKey:
            print("d")
        if "q" in self.listKey:
            self.isRunning = False
            return False
        return True

    def mainLoop(self):
        self.iManager.main()
        if self.isRunning:
            self.getKeyList()
            self.testMove()
            self.dManager.main()
            return True
        else:
            return False
