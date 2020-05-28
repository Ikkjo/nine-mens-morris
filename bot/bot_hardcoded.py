from services.gameboard_service import GameboardService
from repos.active_player import ActivePlayer
import random


def bot_random_place():
    gameboard_state = GameboardService().get_gameboard_state()
    player = ActivePlayer().player
    if GameboardService().is_empty():
        moves = [(1, 1), (3, 1), (4, 1), (6, 1)]
        move = random.choice(moves)
        return move

    else:

        for row in gameboard_state:
            for position in row:
                if position.piece != 'o' and position.piece != player.piece_color:
                    directions = ["up", "down", "left", "right"]

                    random_direction = random.choice(directions)

                    if position.next[random_direction] is None:
                        random_direction = random.choice(directions)

                    if position.next[random_direction] is None:
                        random_direction = random.choice(directions)

                    if position.next[random_direction] is None:
                        random_direction = random.choice(directions)



                    place = position.next[random_direction]

                    place_row = place.row
                    place_column = place.column

                    move = (place_row, place_column)

                    return move
