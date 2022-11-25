import math

class Planet(object):
    def __init__(self, name, radius, distance):

        self.name      = name
        self.radius    = radius
        self.deistance = distance

    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getDistance(self):
        return self.distance

    def calcVolume(self):
        volume = (4.0/3) * math.pi * (self.radius ** 3)
        return volume

    def updateName(self,name):
        self.name = name

        
