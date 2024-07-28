from pygame import Vector2

from Ball import Ball
from Ring import Ring
from utils import utils


class Game:
    def __init__(self):
        self.ball = Ball(Vector2(utils.width/2,utils.height/2),2,(255,255,255))
        self.ring = Ring(Vector2(utils.width/2,utils.height/2),20)

    def update(self):
        utils.world.Step(1.0 / 60.0, 6, 2)

    def draw(self):
        self.ring.draw()
        self.ball.draw()