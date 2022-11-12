from pico2d import *
import random
import game_framework
from state import game_over_state


class Enemy:
    image = None

    def __init__(self):
        if Enemy.image == None:
            Enemy.image = load_image('png/enemy.png')
        self.x, self.y, self.fall_speed = random.randint(100, 1040), 63, 0

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

    def get_bb(self):
        return self.x - 32, self.y - 32, self.x + 32, self.y + 32

    def handle_collision(self, other, group):
        if group == 'floor:enemy':
            self.fall_speed = 0
        if group == 'player:enemy':
            game_framework.change_state(game_over_state)


class FallEnemy(Enemy):

        MIN_FALL_SPEED = 5  # 50 pps = 1.5 meter per sec
        MAX_FALL_SPEED = 20  # 200 pps = 6 meter per sec

        def __init__(self):
            self.x, self.y, self.fall_speed = random.randint(0, 1140), 600, random.randint(
                FallEnemy.MIN_FALL_SPEED, FallEnemy.MAX_FALL_SPEED)
