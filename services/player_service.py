from modules.player import HumanPlayer, BotPlayer
from interface.colour_chooser_menu import colour_chooser_menu
from repos.player_repo import PlayerRepo


class PlayerService(object):

    # noinspection PyUnboundLocalVariable
    @staticmethod
    def new_player(player_type: str, color: str):
        player_types = {"human", "bot"}

        if player_type not in player_types:
            return False

        if player_type == "human":
            player = HumanPlayer(color)

        elif player_type == "bot":
            player = BotPlayer(color)

        return True

    @staticmethod
    def second_player(mode, second_player_color):
        return PlayerService.new_player(mode, second_player_color)
