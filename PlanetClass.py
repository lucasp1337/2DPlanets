import numpy as np


class Planet:
    def __init__(self, name, mass, radius, x, y, color, momentum: np.array = ([0, 0]),
                 acceleration: np.array = ([0, 0]), velocity: np.array = ([0, 0])):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.momentum = momentum
        self.acceleration = acceleration
        self.velocity = velocity

    def setAcceleration(self, acceleration):
        self.acceleration = acceleration

    def getAcceleration(self):
        return self.acceleration

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def update(self, timeframe):
        self.velocity = [self.velocity[0]+self.acceleration[0]*timeframe ,self.velocity[1]+self.acceleration[1]*timeframe]
        self.x += self.velocity[0]*timeframe
        self.y += self.velocity[1]*timeframe
