from pico2d import *
import game_framework
import game_world
from obj.background import Background
from obj.player import Boy


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
    global boy, background
    boy = Boy()
    background = Background()
    game_world.add_object(background, 0)
    game_world.add_object(boy, 1)


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    background.draw()
    boy.draw()
    update_canvas()