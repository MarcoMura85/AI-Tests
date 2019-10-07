import pygame
import math
import collisionClass
import sys
import distanceSensors

class RewardGates():

    def __init__(self, startingGate, rect, surface):

        self.gatesList = []
        self.gatesDict = {}
        self.points1 = []
        self.points2 = []
        self.startingGate = startingGate
        self.currentGate = startingGate
        self.surface = surface
        self.center = (rect[0], rect[1])
        self.width = rect[2]
        self.height = rect[3]

    def loadRewardGates(self, points1, points2):

        self.points1 = points1
        self.points2 = points2
        for pointOut in range(len(points2)):
            distPrev = float('inf')
            for pointIn in range(len(points1)):
                dist = distanceSensors.distance(points1[pointIn], points2[pointOut])
                if dist < distPrev:
                    distPrev = dist
                    self.gatesDict[pointOut] = pointIn

        d2 = {v: k for k, v in self.gatesDict.items()}  # exchange keys, values
        self.gatesDict = {v: k for k, v in d2.items()}   # remove duplicate keys
        self.gatesList = list(self.gatesDict)

    def updateRect(self, rect):
        self.center = (rect[0], rect[1])
        self.width = rect[2]
        self.height = rect[3]

    def drawGates(self, onlyCurrent = False):

        if onlyCurrent:
            color = (0, 255, 0)
            pygame.draw.line(self.surface, color, self.points2[self.gatesList[self.currentGate]],
                             self.points1[self.gatesDict[self.gatesList[self.currentGate]]], 2)
            return

        for i in range(len(self.gatesList)):
            if i == self.currentGate:
                color = (0, 255, 0)
            else:
                color = (255, 255, 0)
            pygame.draw.line(self.surface, color,  self.points2[self.gatesList[i]],  self.points1[self.gatesDict[self.gatesList[i]]], 3)

    def checkGatePass(self, carVertices):

        greenGate = [self.points2[self.gatesList[self.currentGate]], self.points1[self.gatesDict[self.gatesList[self.currentGate]]]]

        if collisionClass.doPolygonIntersect(carVertices, greenGate):

            if self.currentGate < len(self.gatesList)-1:
                self.currentGate += 1
            else:
                self.currentGate = 0

            return True
        else:
            return False
