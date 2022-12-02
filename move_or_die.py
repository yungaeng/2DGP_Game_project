import pico2d
from game import game_framework
from state import title_state

pico2d.open_canvas(1140, 641)
game_framework.run(title_state)
pico2d.close_canvas()
