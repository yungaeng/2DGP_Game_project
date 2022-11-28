from pico2d import *
import game_framework
import game_world

from obj.background import Background
from obj.background import Floor
from obj.player import Player
from obj.enemy import Enemy


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            player.handle_event(event)


player = None
background = None
floor = None
enemy = None


def enter():
    global player, background, floor, enemy

    player = Player()
    background = Background()
    floor = Floor()
    enemy = Enemy()

    game_world.add_object(background, 0)
    game_world.add_object(floor, 0)

    game_world.add_object(enemy, 1)
    game_world.add_object(player, 1)


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()

    background.draw()
    floor.draw()

    player.draw()
    enemy.draw()

    update_canvas()