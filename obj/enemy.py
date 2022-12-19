from pico2d import *
import random
import game_framework
from state import game_over_state


class Enemy:
    MIN_FALL_SPEED = 100
    MAX_FALL_SPEED = 300
    image = None

    def __init__(self):
        if Enemy.image == None:
            Enemy.image = load_image('png/enemy.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1140), 610, random.randint(Enemy.MIN_FALL_SPEED, Enemy.MAX_FALL_SPEED)

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

    def get_bb(self):
        return self.x - 32, self.y - 32, self.x + 32, self.y + 32

    def handle_collision(self, other, group):
        if group == 'floor:enemy':
            self.x = random.randint(0, 1140)
            self.y = 610
        if group == 'player:enemy':
            game_framework.change_state(game_over_state)


