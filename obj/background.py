from pico2d import *


class Background:
    def __init__(self):
        self.image = load_image('png/background.png')

    def draw(self):
        self.image.draw(570, 321)

    def update(self):
        pass


class Floor:
    def __init__(self):
        self.image = load_image('png/floor.png')

    def draw(self):
        self.image.draw(570, 32)

    def update(self):
        pass
