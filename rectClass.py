import pygame
import numpy
import math

class myRect(pygame.Surface):
    def __init__(self, surface, rect, angle):
        self.xpos = rect[0]
        self.ypos = rect[1]
        self.width = rect[2]
        self.height = rect[3]
        self.angle = angle
        self.surface = surface
        self.P0 = (self.xpos, self.ypos)
        self.P1 = (self.xpos, self.ypos+self.height)
        self.P2 = (self.xpos+self.width, self.ypos+self.height)
        self.P3 = (self.xpos+self.width, self.ypos)

    def updateRect(self, rect):
        self.xpos = rect[0]
        self.ypos = rect[1]
        self.width = rect[2]
        self.height = rect[3]
        self.P0 = (self.xpos, self.ypos)
        self.P1 = (self.xpos, self.ypos + self.height)
        self.P2 = (self.xpos + self.width, self.ypos + self.height)
        self.P3 = (self.xpos + self.width, self.ypos)

    def updatePos(self, xpos, ypos, angle):
        self.xpos = xpos - self.width/2
        self.ypos = ypos - self.height/2
        self.angle = angle

        self.P0 = (self.xpos, self.ypos)
        self.P1 = (self.xpos, self.ypos + self.height)
        self.P2 = (self.xpos + self.width, self.ypos + self.height)
        self.P3 = (self.xpos + self.width, self.ypos)

        self.P0 = self.rotatePoint((xpos, ypos), self.P0, angle)
        self.P1 = self.rotatePoint((xpos, ypos), self.P1, angle)
        self.P2 = self.rotatePoint((xpos, ypos), self.P2, angle)
        self.P3 = self.rotatePoint((xpos, ypos), self.P3, angle)

    def rotatePoint(self, origin, point, angle):
        ox, oy = origin
        px, py = point

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return (qx, qy)

    def drawMyRect(self):
        pygame.draw.line(self.surface, (0, 0, 255), self.P0, self.P1)
        pygame.draw.line(self.surface, (0, 0, 255), self.P1, self.P2)
        pygame.draw.line(self.surface, (0, 0, 255), self.P2, self.P3)
        pygame.draw.line(self.surface, (0, 0, 255), self.P3, self.P0)



    #def rotate(self, angle):
      #(your rotation code goes here)