from pico2d import *
import game_framework
import game_world

from obj.score import Score


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()


score = None


def enter():
    global score

    score = Score()

    game_world.add_object(score.image, 0)
    game_world.add_object(score.font, 1)


def exit():
    game_world.clear()


def update():
    pass


def draw():
    clear_canvas()
    score.draw()
    update_canvas()


