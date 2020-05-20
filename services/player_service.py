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

    @staticmethod
    def next_move(active_player, move_mode):
        player_type = active_player.type

        successful = False

        if player_type == "human":
            successful = PlayerService._human_next_move(active_player, move_mode)

        elif player_type == "bot":
            successful = PlayerService._bot_next_move(active_player, move_mode)

        return successful

    @staticmethod
    def _human_next_move(player):
        piece_to_move = PlayerService._piece_to_move(player)
        position_to_move = PlayerService._position_to_move()

    @staticmethod
    def _piece_to_move(player):
        moving_piece = colour_chooser_menu()
        if moving_piece is None:
            print()
        pass

    @staticmethod
    def _position_to_move(player):

        pass

    @staticmethod
    def _bot_next_move(player, move_mode):
        pass

# TODO: _piece_to_move
# TODO: _position_to_move