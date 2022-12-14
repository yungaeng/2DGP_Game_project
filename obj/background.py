from pico2d import *


class Background:
    def __init__(self):
        self.image = load_image('png/background.png')
        self.font = load_font('font/ENCR10B.TTF', 20)
        self.bgm = load_music('sound/bgm.mp3')
        self.bgm.set_volume(25)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(570, 321)
        self.font.draw(10, 620, f'(Time: {get_time():.2f})', (0, 255, 0))

    def update(self):
        pass


class Floor:
    def __init__(self):
        self.image = load_image('png/floor.png')

    def draw(self):
        self.image.draw(570, 32)

    def get_bb(self):
        return 0, 0, 1600 - 1, 63

    def handle_collision(self, other, group):
        pass

    def update(self):
        pass

