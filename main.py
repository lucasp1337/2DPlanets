import pygame
import numpy as np
import scipy
import scipy.constants

from PlanetClass import Planet


def drawPlanets(Planets):
    for planet in Planets:
        pygame.draw.circle(screen, planet.color, [planet.x, planet.y], planet.radius)
        print(planet.name ,planet.x, planet.y)


def unitVector(vector: np.array) -> np.array:
    x = vector[0]
    y = vector[1]
    n = np.sqrt((x * x + y * y))
    if(n != 0):
        return [x / n, y / n]
    else:
        return vector


def scalarMultiplication(vector: np.array, num) -> np.array:
    return [vector[0] * num, vector[1] * num]


def vectorLength(vector: np.array) -> float:
    return np.sqrt(vector[0] * vector[0] + vector[1] * vector[1])


def computeGravitationalForces(Planets):
    for i in range(0, len(Planets), 1):
        for k in range(i + 1, len(Planets), 1):
            mass1 = Planets[i].mass
            mass2 = Planets[k].mass
            x1 = Planets[i].x
            y1 = Planets[i].y
            x2 = Planets[k].x
            y2 = Planets[k].y
            r12 = np.array([x2 - x1, y2 - y1])
            r21 = -r12
            g1 = (mass2 * scipy.constants.G) / vectorLength(r12)
            g2 = (mass1 * scipy.constants.G) / vectorLength(r21)
            r12 = unitVector(r12)
            r21 = unitVector(r12)
            r12 = scalarMultiplication(r12, g1)
            r21 = scalarMultiplication(r21, g2)
            Planets[i].setAcceleration(r12)
            Planets[k].setAcceleration(r21)


def updatePlanetStats(Planets):
    for planet in Planets:
        planet.update(1/60) # since the fps is 60, we want the dt to be 1/60 of  a second.


def computePhysics(Planets):
    computeGravitationalForces(Planets)
    updatePlanetStats(Planets)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    timeframe = 1 / 60
    Planets = [Planet('Earth', 5.972e4, 20, 1280/2 + 300, 720 / 2, "Blue"),
               Planet('Moon', 7.34767309e3, 20, 1280/2 + 400, 100, "Gray"),
               Planet('Sun', 1.989e4, 20, 1280/2, 720/2, "Yellow")]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("purple")
        computePhysics(Planets)
        # RENDER YOUR GAME HERE
        drawPlanets(Planets)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
