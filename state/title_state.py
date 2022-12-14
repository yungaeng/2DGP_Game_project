from state import play_state
from game import game_framework

from pico2d import *
image = None


def enter():
    global image
    image = load_image('png/title.png')


def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_SPACE:
                    game_framework.change_state(play_state)


def draw():
    clear_canvas()
    image.draw(570, 321)
    update_canvas()


def update():
    pass






