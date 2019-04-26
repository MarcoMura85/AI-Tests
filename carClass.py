import pygame

class Car:

    def __init__(self, x, y, image):
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
        self.RotateNeg = False

    def showCar(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def updatePosition(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_UP:
                    up = True
                if event.key == pygame.K_DOWN:
                    down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_DOWN:
                    down = False

        # update the position of the smily
        if left: xpos -= step_x
        if right: xpos += step_x
        if up: ypos -= step_y
        if down: ypos += step_y