import pygame
import math

class Car:

    def __init__(self, x, y, image, surface):
        self.x = x
        self.y = y
        self.angle = 0
        self.vel = [0, 0]
        self.acc = 0
        self.image = pygame.image.load(image)
        self.size = self.image.get_rect().size
        self.forward = False
        self.backward = False
        self.rotatePos = False
        self.rotateNeg = False
        self.surface = surface

    def setPos (self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def showCar(self, surface):
        self.move()

        degrees = math.degrees(self.angle)
        rot_img = pygame.transform.rotate(self.image, -degrees)
        rect = rot_img.get_rect(center=(self.x, self.y))

        #surface.fill((128, 128, 128))
        surface.blit(rot_img, rect)

        #self.image = pygame.transform.rotate(self.image, self.angle)
        #surface.blit(self.image, (self.x, self.y))

    def updatePosition(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rotatePos = True
            if event.key == pygame.K_RIGHT:
                self.rotateNeg = True
            if event.key == pygame.K_UP:
                self.forward = True
            if event.key == pygame.K_DOWN:
                self.backward = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.rotatePos = False
            if event.key == pygame.K_RIGHT:
                self.rotateNeg = False
            if event.key == pygame.K_UP:
                self.forward = False
            if event.key == pygame.K_DOWN:
                self.backward = False

        # update the position of the car
        if self.rotatePos: self.angle -= 0.1
        if self.rotateNeg: self.angle += 0.1
        if self.forward : self.acc += 1
        if self.backward : self.acc = 0

        if self.acc <-1 : self.acc = -1
        if self.acc > 1 : self.acc = 1

        self.showCar(self.surface)

    def move(self):
        self.vel[0]=self.acc * math.sin(self.angle)
        self.vel[1] = self.acc * math.cos(self.angle)
        self.x +=self.vel[0]
        self.y -=self.vel[1]