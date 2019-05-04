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

        self.sFront = (0,0)
        self.sFrontLeft = (0,0)
        self.sFrontRight = (0,0)
        self.sRight = (0,0)
        self.sLeft = (0,0)
        self.sBack = (0,0)
        self.sBackRight = (0,0)
        self.sBackLeft = (0,0)

        self.updatePos(self.center[0], self.center[1], self.angle)

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

        sensors = [self.sFront, self.sFrontLeft, self.sFrontRight,
                        self.sRight, self.sLeft, self.sBack, self.sBackRight, self.sBackLeft]

        for i in range(len(sensors)):
            pygame.draw.line(self.surface, color, self.center, sensors[i])


    def drawInterceptionPoint(self, lines):

        sensors = [self.sFront, self.sFrontLeft, self.sFrontRight,
                        self.sRight, self.sLeft, self.sBack, self.sBackRight, self.sBackLeft]

        points = []

        for i in range(len(sensors)):
            pp = lines_interseptions([self.center, sensors[i]], lines)
            if len(pp) > 0:
                points += pp

        for i in range(len(points)):
            pygame.draw.circle(self.surface, (0, 0, 255), points[i], 5)

def segment_intersection(line1, line2):

    if not collisionClass.doSegmentIntersect(line1[0],line1[1], line2[0],line2[1]):
        raise Exception('segment do not intersect')

    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('segment do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    return round(x), round(y)

def lines_interseptions (listPoint1, listPoint2):
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
                interception = segment_intersection(line1, line2)
                interceptions.append(interception)
            except:
                continue

    return interceptions



