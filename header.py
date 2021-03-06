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
        self.DISPLAY_WIDTH = 1000
        self.DISPLAY_HEIGHT = 500
        self.lenCell = 20
        self.colarBlock = (0, 100, 0)
        self.colarEmpty = (255, 255, 255)
        self.screen = pygame.display.set_mode(
            (self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        pygame.display.set_caption("tetris")
        self.oldTime = pygame.time.get_ticks

    def drawReactAsBoard(self, board):
        y = self.DISPLAY_HEIGHT
        x_0 = self.DISPLAY_WIDTH / 2 - \
            self.lenCell * len(board[0]) / 2
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                left = x_0 + j * self.lenCell
                top = 30 + i * self.lenCell
                rect = Rect(left, top, self.lenCell, self.lenCell)
                if board[i][j] == 0:
                    self.drawReact(self.colarEmpty, rect)
                else:
                    self.drawReact(self.colarBlock, rect)

    def drawReact(self, colar, rect):
        pygame.draw.rect(self.screen, colar, rect)

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
        board = [[0] * 10 for i in range(20)]
        self.drawReactAsBoard(self.gManager.board)
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
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]
        self.listMino = [
            [[1, 1, 1, 1],
             [0, 0, 0, 0]],
            [[1, 1, 0, 0],
             [0, 1, 1, 0]],
            [[0, 0, 1, 1],
             [0, 1, 1, 0]],
            [[0, 1, 1, 0],
             [0, 1, 1, 0]],
            [[0, 1, 1, 1],
             [0, 0, 0, 1]],
            [[1, 1, 1, 0],
             [1, 0, 0, 0]],
            [[1, 1, 1, 0],
             [0, 1, 0, 0]]
        ]
        return

    def addMinoToBoard(self):
        board = self.board
        for i in range(0, len(self.listMino[0])):
            for j in range(0, len(self.listMino[0][i])):
                if self.listMino[0][i][j] == 1:
                    self.board[i][j] = 1

    def getKeyList(self):
        self.listKey = self.iManager.main()

    def testMove(self):
        pygame.event.pump()  # ???????????????(???????????????????????????????????????????????????????????????)
        print(self.listKey)
        if "w" in self.listKey:
            self.addMinoToBoard()
            pass
        if "a" in self.listKey:
            pass
        if "s" in self.listKey:
            print(self.board)
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
