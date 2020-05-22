from modules.player import HumanPlayer, BotPlayer
from interface.colour_chooser_menu import colour_chooser_menu
from repos.player_repo import PlayerRepo


class PlayerService(object):

    # noinspection PyUnboundLocalVariable
    @staticmethod
    def new_player(player_type: str, color: str):
        player_types = {"human", "bot"}

        if player_type not in player_types:
            return None

        if player_type == "human":
            player = HumanPlayer(color)

        elif player_type == "bot":
            player = BotPlayer(color)

        return player

    @staticmethod
    def input_conversion(user_input):
        row_map = {"A1": (0,0), "A4": (0,1), "A7": (0,2),
                   "B2": (1,0), "B4": (1,1), "B6": (1,2),
                   "C3": (2,0), "C4": (2,1), "C5": (2,2),
                   "D1": (3,0), "D2": (3,1), "D3": (3,2),
                   "D5": (4,0), "D6": (4,1), "D7": (4,2),
                   "E3": (5,0), "E4": (5,1), "E5": (5,2),
                   "F2": (6,0), "F4": (6,1), "F6": (6,2),
                   "G1": (7,0), "G4": (7,1), "G7": (7,2),}

        return row_map[user_input]
