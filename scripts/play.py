from interface.clear_screen import clear_screen
from interface.draw_gameboard import draw_gameboard
from scripts.change_active_player import change_active_player
from scripts.play_mill import play_mill

def play(play_mode, finishing_condition):
    while finishing_condition():
        clear_screen()
        draw_gameboard()
        mill = play_mode()
        if mill:
            play_mill()
        change_active_player()

