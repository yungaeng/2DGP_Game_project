from pico2d import *

def handle_events():
    global running, x, dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

open_canvas()

background = load_image('background.png')
character = load_image('anisheet.png')

running = True
x = 800 // 2
frame = 0
dir = 0

while running:
    clear_canvas()
    background.draw(400, 300)
    if dir == 1:
        character.clip_draw(frame * 100, 0, 100, 100, x, 100)
    elif dir == -1:
        character.clip_draw(frame * 100, 200, 100, 100, x, 100)
    else :
        character.clip_draw(frame * 100, 700, 100, 100, x, 100)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 3
    x += dir * 5
    delay(0.01)

close_canvas()