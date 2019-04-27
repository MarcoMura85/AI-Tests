import pygame

class myRect(pygame.Surface):
    def __init__(self, surface, rect, angle):
      self.xpos = rect[0]
      self.ypos = rect[1]
      self.width = rect[2]
      self.height = rect[3]
      self.angle = angle
      self.surface = surface

    def updateRect(self, rect):
        self.xpos = rect[0]
        self.ypos = rect[1]
        self.width = rect[2]
        self.height = rect[3]

    def updatePos(self, xpos, ypos, angle):
        self.xpos = xpos - self.width/2
        self.ypos = ypos - self.height/2
        self.angle = angle

    def drawMyRect(self):
        pygame.draw.line(self.surface, (0, 0, 255), (self.xpos, self.ypos), (self.xpos, self.ypos+self.height))
        pygame.draw.line(self.surface, (0, 0, 255), (self.xpos, self.ypos), (self.xpos+self.width, self.ypos))
        pygame.draw.line(self.surface, (0, 0, 255), (self.xpos+self.width, self.ypos+self.height), (self.xpos+self.width, self.ypos))
        pygame.draw.line(self.surface, (0, 0, 255), (self.xpos+self.width, self.ypos+self.height), (self.xpos, self.ypos+self.height))



    #def rotate(self, angle):
      #(your rotation code goes here)