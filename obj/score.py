from pico2d import *


class Score:
    def __init__(self):
        self.image = load_image('png/game_over.png')
        self.font = load_font('font/ENCR10B.TTF', 25)
        self.final_score = int(get_time()) * 100

    def draw(self):
        self.image.draw(570, 321)
        self.font.draw(200, 330, f'{self.final_score}', (255, 255, 255))

    def update(self):
        pass