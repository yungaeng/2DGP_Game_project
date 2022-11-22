import pico2d
from pico2d import *
import game_framework
from obj.background import Background
from obj.boy import Boy


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


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