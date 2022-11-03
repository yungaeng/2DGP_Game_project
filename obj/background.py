from pico2d import *


class Background:
    def __init__(self):
        self.image = load_image('png/background.png')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass
