import pico2d
import game_framework
from state import title_state

pico2d.open_canvas(1140, 640)
game_framework.run(title_state)
pico2d.close_canvas()
