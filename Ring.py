import math

import pygame
from Box2D import b2EdgeShape, Box2D

from utils import utils


class Ring:
    def __init__(self, pos, radius):
        self.color = (255,255,255)
        self.radius = radius

        self.size = 360
        self.vertices = []
        for i in range(self.size):
            angle = i * (2 * math.pi / self.size)
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            self.vertices.append((x, y))

        self.body = utils.world.CreateStaticBody(position=utils.from_Pos(pos))
        self.body.userData = self

        self.create_edge_shape()

    def create_edge_shape(self):
        for i in range(self.size):
            angle = i * (360 / self.size)
            if (0 <= angle <= 90) or (140 <= angle <= 360):
                v1 = self.vertices[i]
                v2 = self.vertices[(i + 1) % self.size]
                edge = b2EdgeShape(vertices=[v1, v2])
                self.body.CreateEdgeFixture(shape=edge, density=1, friction=0.0, restitution=1.0)

    def draw(self):
        self.draw_edges()

    def draw_edges(self):
        for fixture in self.body.fixtures:
            v1 = utils.to_Pos(self.body.transform * fixture.shape.vertices[0])
            v2 = utils.to_Pos(self.body.transform * fixture.shape.vertices[1])
            pygame.draw.line(utils.screen, self.color, v1, v2, 2)

