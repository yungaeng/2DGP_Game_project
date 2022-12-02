from pico2d import *

from game import game_framework, game_world

from obj.background import Background, Floor
from obj.player import Player
from obj.enemy import Enemy

background = None
player = None
floor = None
all_enemy = []


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            player.handle_event(event)


def enter():
    global background, floor, player

    background = Background()
    game_world.add_object(background, 0)
    floor = Floor()
    game_world.add_object(floor, 0)
    player = Player()
    game_world.add_object(player, 1)

    global all_enemy
    all_enemy = [Enemy() for i in range(10)]
    game_world.add_objects(all_enemy, 1)

    game_world.add_collision_pairs(player, all_enemy, 'player:enemy')
    game_world.add_collision_pairs(floor, all_enemy, 'floor:enemy')


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()

