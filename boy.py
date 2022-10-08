from pico2d import *


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
        self. dir = 0
        self.image = load_image('anisheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.base_frame = (self.base_frame + 1) % 2
        self.x += self.dir * 1

        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.base_frame * 100, 700, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    running = False
                case pico2d.SDLK_LEFT:
                    boy.dir -= 1
                case pico2d.SDLK_RIGHT:
                    boy.dir += 1
        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_LEFT:
                    boy.dir += 1
                case pico2d.SDLK_RIGHT:
                    boy.dir -= 1


open_canvas()

boy = Boy()
background = Background()

running = True

while running:
    handle_events()

    boy.update()

    clear_canvas()
    background.draw()
    boy.draw()
    update_canvas()

    delay(0.001)