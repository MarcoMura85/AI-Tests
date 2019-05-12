import pygame
import math
import collisionClass
import sys

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

        self.sFrontDis = float('inf')
        self.sFrontLeftDis = float('inf')
        self.sFrontRightDis = float('inf')
        self.sRightDis = float('inf')
        self.sLeftDis = float('inf')
        self.sBackDis = float('inf')
        self.sBackRightDis = float('inf')
        self.sBackLeftDis = float('inf')

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
        scale = 7.5

        self.sFront = (self.center[0], self.center[1] - (self.height*scale))
        self.sRight = (self.center[0] + (self.height*scale), self.center[1])
        self.sLeft = (self.center[0] - (self.height*scale), self.center[1])
        self.sBack = (self.center[0], self.center[1] + (self.height*scale))

        self.sFront = self.rotatePoint((xpos, ypos), self.sFront, self.angle)
        self.sBack = self.rotatePoint((xpos, ypos), self.sBack, self.angle)
        self.sRight = self.rotatePoint((xpos, ypos), self.sRight, self.angle)
        self.sLeft = self.rotatePoint((xpos, ypos), self.sLeft, self.angle)
        self.sFrontLeft = self.rotatePoint(self.center, self.sFront, math.radians(45))
        self.sFrontRight = self.rotatePoint(self.center, self.sFront, math.radians(-45))
        self.sBackRight = self.rotatePoint(self.center, self.sBack, math.radians(-45))
        self.sBackLeft = self.rotatePoint(self.center, self.sBack, math.radians(45))

    def updateSensorsDistances(self, sensorsDist):

        self.sFrontDis = sensorsDist[0]
        self.sFrontLeftDis = sensorsDist[1]
        self.sFrontRightDis = sensorsDist[2]
        self.sRightDis = sensorsDist[3]
        self.sLeftDis = sensorsDist[4]
        self.sBackDis = sensorsDist[5]
        self.sBackRightDis = sensorsDist[6]
        self.sBackLeftDis = sensorsDist[7]


    def calcInterseptions(self, lines):
        sensors = [self.sFront, self.sFrontLeft, self.sFrontRight,
                   self.sRight, self.sLeft, self.sBack, self.sBackRight, self.sBackLeft]

        points = []
        distances = []

        for i in range(len(sensors)):
            dis = sys.maxsize
            tt = float('inf')
            pp = lines_interseptions([self.center, sensors[i]], lines)
            if len(pp) > 0:
                for i in range(len(pp)):
                    tt = distance(self.center, pp[i])
                    if tt < dis:
                        nearIntersect = pp[i]
                        dis = tt

                points.append(nearIntersect)

            distances.append(tt)

        return points, distances

    def calcInterseptionCircuit(self, inner, outer):
        pointIn, distIn = self.calcInterseptions(inner)
        pointOut, distOut = self.calcInterseptions(outer)

        sensorsDistances = [self.sFrontDis, self.sFrontLeftDis, self.sFrontRightDis,
                            self.sRightDis, self.sLeftDis, self.sBackDis, self.sBackRightDis, self.sBackLeftDis]
        distances = []

        for i in range(len(sensorsDistances)):
            if distIn[i] < distOut[i]:
                sensorsDistances[i] = distIn[i]
                continue
            sensorsDistances[i] = distOut[i]

        self.updateSensorsDistances(sensorsDistances)

        #print(sensorsDistances)

        return pointIn+pointOut, distIn

    def drawSensors(self):
        color = (255, 255, 255)

        sensors = [self.sFront, self.sFrontLeft, self.sFrontRight,
                        self.sRight, self.sLeft, self.sBack, self.sBackRight, self.sBackLeft]

        for i in range(len(sensors)):
            pygame.draw.line(self.surface, color, self.center, sensors[i])


    def drawInterceptionPoint(self, points):
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
                if not interception in interceptions :
                    interceptions.append(interception)
            except:
                continue

    return interceptions


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
