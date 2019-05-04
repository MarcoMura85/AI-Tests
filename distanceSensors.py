import pygame
import math
import collisionClass

class MySensors():

    def __init__(self, surface, rect, angle):

        self.center = (rect[0], rect[1])
        self.width = rect[2]
        self.height = rect[3]
        self.angle = angle
        self.surface = surface

        self.sFront = (self.center[0], self.center[1]-self.width)
        self.sFrontLeft = self.rotatePoint(self.center, self.sFront, self.angle+math.radians(45))
        self.sFrontRight = (self.center[0], self.center[1])
        self.sRight = (self.center[0], self.center[1])
        self.sLeft = (self.center[0], self.center[1])
        self.sBack = (self.center[0], self.center[1])
        self.sBackRight = (self.center[0], self.center[1])
        self.sBackLeft = (self.center[0], self.center[1])

    def rotatePoint(self, origin, point, angle):
        ox, oy = origin
        px, py = point

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return qx, qy

    def updateRect(self, rect):
        self.center = (rect[0], rect[1])
        self.width = rect[2]
        self.height = rect[3]

    def updatePos(self, xpos, ypos, angle):
        self.center = (xpos, ypos)
        self.angle = angle

        self.sFront = (self.center[0], self.center[1] - (self.height*1.8))
        self.sRight = (self.center[0] + (self.height*1.8), self.center[1])
        self.sLeft = (self.center[0] - (self.height*1.8), self.center[1])
        self.sBack = (self.center[0], self.center[1] + (self.height*1.8))

        self.sFront = self.rotatePoint((xpos, ypos), self.sFront, self.angle)
        self.sBack = self.rotatePoint((xpos, ypos), self.sBack, self.angle)
        self.sRight = self.rotatePoint((xpos, ypos), self.sRight, self.angle)
        self.sLeft = self.rotatePoint((xpos, ypos), self.sLeft, self.angle)
        self.sFrontLeft = self.rotatePoint(self.center, self.sFront, math.radians(45))
        self.sFrontRight = self.rotatePoint(self.center, self.sFront, math.radians(-45))
        self.sBackRight = self.rotatePoint(self.center, self.sBack, math.radians(-45))
        self.sBackLeft = self.rotatePoint(self.center, self.sBack, math.radians(45))


    def drawSensors(self):
        color = (255, 255, 255)
        pygame.draw.line(self.surface, color, self.center, self.sFront)
        pygame.draw.line(self.surface, color, self.center, self.sBack)
        pygame.draw.line(self.surface, color, self.center, self.sRight)
        pygame.draw.line(self.surface, color, self.center, self.sLeft)
        pygame.draw.line(self.surface, color, self.center, self.sFrontLeft)
        pygame.draw.line(self.surface, color, self.center, self.sFrontRight)
        pygame.draw.line(self.surface, color, self.center, self.sBackRight)
        pygame.draw.line(self.surface, color, self.center, self.sBackLeft)



    def drawInterceptionPoint(self, lines):
        pf = lines_interceptions([self.center, self.sFront], lines)
        pb = lines_interceptions([self.center, self.sBack], lines)
        pl = lines_interceptions([self.center, self.sLeft], lines)
        pr = lines_interceptions([self.center, self.sRight], lines)

        points = pb+pf+pl+pr
        for i in range(len(points)):
            pygame.draw.circle(self.surface, (0, 0, 255), points[i], 5)

def line_intersection(line1, line2):

    if not collisionClass.doSegmentIntersect(line1[0],line1[1], line2[0],line2[1]):
        raise Exception('lines do not intersect')

    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    return round(x), round(y)

def lines_interceptions (listPoint1, listPoint2):
    interceptions = []
    for i in range(len(listPoint1)):
        if i == (len(listPoint1) - 1):
            line1 = (listPoint1[i], listPoint1[0])
        else:
            line1 = (listPoint1[i], listPoint1[i+1])

        for j in range(len(listPoint2)):
            if j == (len(listPoint2) - 1):
                line2 = (listPoint2[j], listPoint2[0])
            else:
                line2 = (listPoint2[j], listPoint2[j + 1])
            try:
                interception = line_intersection(line1, line2)
                interceptions.append(interception)
            except:
                continue

    return interceptions



