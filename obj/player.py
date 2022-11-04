from pico2d import *

# 이벤트 정의
RD, LD, RU, LU = range(4)

key_event_table = {
(SDL_KEYDOWN, SDLK_RIGHT): RD,
(SDL_KEYDOWN, SDLK_LEFT): LD,
(SDL_KEYUP, SDLK_RIGHT): RU,
(SDL_KEYUP, SDLK_LEFT): LU
}


class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0

    @staticmethod
    def exit(self):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

        if self.jump > 0:
            self.jump -= 1

    @staticmethod
    def draw(self):
        self.image.clip_draw(self.frame * 96, 312, 96, 104, self.x, self.y + self.jump)


class RUN:
    @staticmethod
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    @staticmethod
    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 1140)

        if self.y == 64:
            self.sig = 0
        elif self.sig == 1:
            self.jump -= 1

    @staticmethod
    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 96, 0, 96, 104, self.x, self.y + self.jump)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 96, 208, 96, 104, self.x, self.y + self.jump)


next_state = {
    IDLE: {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN},
    RUN:  {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE}
}


class Player:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 0
        self.jump = 0
        self.sig = 0
        self.image = load_image('png/player.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

        if self.y == 64:
            self.sig = 0
        elif self.sig == 1:
            self.jump -= 1

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

        if event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_SPACE:
                    if self.sig == 0:
                        self.jump += 150
                case pico2d.SDLK_UP:
                    if self.sig == 0:
                        self.jump += 150
