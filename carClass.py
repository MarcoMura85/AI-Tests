import pygame
import rectClass
import math

class Car:

    def __init__(self, x, y, image, surface):

        self.maxAcc = 1
        self.zeroAcc = 0.15
        self.angleStep = 0.15
        self.brakeStep = 0.15
        self.accStep = 1

        self.x = x
        self.y = y
        self.angle = 0
        self.vel = [0, 0]
        self.acc = 0
        self.image = pygame.image.load(image)

        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()

        self.myRect22 = rectClass.myRect(surface, self.rect, self.angle)

        self.forward = False
        self.backward = False
        self.rotatePos = False
        self.rotateNeg = False
        self.brake = False
        self.surface = surface
        self.scaleCar(0.3)

    def scaleCar(self, ratio):
        width = round (self.size[0] * ratio)
        height = round(self.size[1] * ratio)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.myRect22.updateRect(self.rect)

    def setPos (self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.myRect22.updatePos(x, y, angle)

    def showCar(self, surface):
        self.move()

        degrees = math.degrees(self.angle)
        rot_img = pygame.transform.rotate(self.image, -degrees)
        self.rect = rot_img.get_rect(center=(self.x, self.y))
        surface.blit(rot_img, self.rect)
        self.myRect22.drawMyRect()
        #pygame.draw.rect(self.surface, (255, 0, 0),self.rect,2)

        #print(self.rect)

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
            if event.key == pygame.K_SPACE:
                self.brake = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.rotatePos = False
            if event.key == pygame.K_RIGHT:
                self.rotateNeg = False
            if event.key == pygame.K_UP:
                self.forward = False
            if event.key == pygame.K_DOWN:
                self.backward = False
            if event.key == pygame.K_SPACE:
                self.brake = False

        # update the position of the car
        if self.rotatePos:
            self.angle -= self.angleStep
        if self.rotateNeg:
            self.angle += self.angleStep
        if self.forward:
            self.acc += self.accStep
        if self.backward:
            self.acc -= self.accStep
        if self.brake and self.acc != 0:
            if self.acc > self.zeroAcc:
                self.acc -= self.brakeStep
            elif self.acc < -self.zeroAcc:
                self.acc += self.brakeStep
            elif -self.zeroAcc < self.acc < self.zeroAcc:
                self.acc = 0

        if self.acc < -self.maxAcc:
            self.acc = -self.maxAcc
        if self.acc > self.maxAcc:
            self.acc = self.maxAcc

        self.showCar(self.surface)

    def move(self):
        self.vel[0] = self.acc * math.sin(self.angle)
        self.vel[1] = self.acc * (math.cos(self.angle))
        self.x += self.vel[0]
        self.y -= self.vel[1]
        self.myRect22.updatePos(self.x, self.y, self.angle)
