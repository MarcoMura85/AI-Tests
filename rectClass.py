import pygame

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
        self.P0 = (self.xpos, self.ypos)
        self.P1 = (self.xpos, self.ypos + self.height)
        self.P2 = (self.xpos + self.width, self.ypos + self.height)
        self.P3 = (self.xpos + self.width, self.ypos)
        self.angle = angle

    def drawMyRect(self):
        pygame.draw.line(self.surface, (0, 0, 255), self.P0, self.P1)
        pygame.draw.line(self.surface, (0, 0, 255), self.P1, self.P2)
        pygame.draw.line(self.surface, (0, 0, 255), self.P2, self.P3)
        pygame.draw.line(self.surface, (0, 0, 255), self.P3, self.P0)



    #def rotate(self, angle):
      #(your rotation code goes here)