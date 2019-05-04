import pygame
import rectClass
import distanceSensors
import math


class Car:

    def __init__(self, x, y, image, surface):

        self.maxAcc = 3
        self.zeroAcc = 0.15
        self.angleStep = 0.15
        self.brakeStep = 0.15
        self.accStep = 1
        self.scaleFactor = 0.3

        self.x = x
        self.y = y
        self.angle = 0
        self.vel = [0, 0]
        self.acc = 0
        self.image = pygame.image.load(image)
        self.surface = surface

        self.rect = self.image.get_rect()
        self.size = self.rect.size

        self.myRect = rectClass.MyRect(self.surface, self.rect, self.angle)
        self.sensors = distanceSensors.MySensors(self.surface, self.rect, self.angle)

        self.forward = False
        self.backward = False
        self.rotatePos = False
        self.rotateNeg = False
        self.brake = False
        self.scaleCar(self.scaleFactor)

    def scaleCar(self, ratio):
        width = round (self.size[0] * ratio)
        height = round(self.size[1] * ratio)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.myRect.updateRect(self.rect)
        self.sensors.updateRect(self.rect)

    def setPos (self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.myRect.updatePos(x, y, angle)
        self.sensors.updatePos(x, y, angle)

    def showCar(self, surface, collision=False):
        self.move()
        degrees = math.degrees(self.angle)

        rot_img = pygame.transform.rotate(self.image, -degrees)
        self.rect = rot_img.get_rect(center=(self.x, self.y))
        surface.blit(rot_img, self.rect)
        self.myRect.drawMyRect(collision)
        self.sensors.drawSensors()

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

    def move(self):
        self.vel[0] = self.acc * math.sin(self.angle)
        self.vel[1] = self.acc * (math.cos(self.angle))
        self.x += self.vel[0]
        self.y -= self.vel[1]
        self.myRect.updatePos(self.x, self.y, self.angle)
        self.sensors.updatePos(self.x, self.y, self.angle)


    def getCarVertices(self):
        return self.myRect.vertices
