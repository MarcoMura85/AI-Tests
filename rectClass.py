import pygame
import math

class MyRect(pygame.Surface):

    def __init__(self, surface, rect, angle):

        self.xpos = rect[0]
        self.ypos = rect[1]
        self.width = rect[2]
        self.height = rect[3]
        self.angle = angle
        self.surface = surface

        self.vertices = [(self.xpos, self.ypos),
                         (self.xpos, self.ypos+self.height),
                         (self.xpos+self.width, self.ypos+self.height),
                         (self.xpos+self.width, self.ypos)]

    def updateRect(self, rect):
        self.xpos = rect[0]
        self.ypos = rect[1]
        self.width = rect[2]
        self.height = rect[3]
        self.vertices[0] = (self.xpos, self.ypos)
        self.vertices[1] = (self.xpos, self.ypos + self.height)
        self.vertices[2] = (self.xpos + self.width, self.ypos + self.height)
        self.vertices[3] = (self.xpos + self.width, self.ypos)

    def updatePos(self, xpos, ypos, angle):
        self.xpos = xpos - self.width/2
        self.ypos = ypos - self.height/2
        self.angle = angle

        self.vertices[0] = (self.xpos, self.ypos)
        self.vertices[1] = (self.xpos, self.ypos + self.height)
        self.vertices[2] = (self.xpos + self.width, self.ypos + self.height)
        self.vertices[3] = (self.xpos + self.width, self.ypos)

        for i in range(len(self.vertices)):
            self.vertices[i] = self.rotatePoint((xpos, ypos), self.vertices[i], angle)

    def rotatePoint(self, origin, point, angle):
        ox, oy = origin
        px, py = point

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return qx, qy

    def drawMyRect(self, collision=False):

        color = (0, 0, 255)
        if collision:
            color = (255, 0, 0)

        pygame.draw.polygon(self.surface, color, self.vertices, 3)