import pico2d
from pico2d import *

import game_framework


class Background:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(400, 300)


class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.base_frame = 0
        self.dir = 0
        self.jump = 0
        self.image = load_image('anisheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.base_frame = (self.base_frame + 1) % 1
        self.x += self.dir * 1

        if self.jump > 0:
            self.jump -= 1

        if self.x > 800:
            self.x = 800
        elif self.x < 0:
            self.x = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y + self.jump)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y + self.jump)
        else:
            self.image.clip_draw(self.base_frame * 100, 700, 100, 100, self.x, self.y + self.jump)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_LEFT:
                    boy.dir -= 1
                case pico2d.SDLK_RIGHT:
                    boy.dir += 1
                case pico2d.SDLK_SPACE:
                    boy.jump += 100
                case pico2d.SDLK_UP:
                    boy.jump += 100
        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_LEFT:
                    boy.dir += 1
                case pico2d.SDLK_RIGHT:
                    boy.dir -= 1


boy = None
background = None
running = True


def enter():
    global boy, background, running
    boy = Boy()
    background = Background()
    running = True


def exit():
    global boy, background, running
    del boy
    del background


def update():
    boy.update()


def draw():
    clear_canvas()
    background.draw()
    boy.draw()
    update_canvas()