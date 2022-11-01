import pico2d
import game_framework
from state import logo_state

pico2d.open_canvas()
game_framework.run(logo_state)
pico2d.close_canvas()
