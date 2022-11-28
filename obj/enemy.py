from pico2d import *


class Enemy:
    def __init__(self):
        self.x, self.y = 800, 64
        self.image = load_image('png/enemy.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
