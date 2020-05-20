from modules.player import HumanPlayer, BotPlayer
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
    def next_move(player):
        player_type = PlayerService._get_player_type(player)

        successful = False

        if player == "human":
            successful = PlayerService._human_next_move(player)


        elif player == "bot":
            successful = PlayerService._bot_next_move(player)

        return successful


    @staticmethod
    def _get_player_type(player):
        player_type = type(player)
        return "human" if player_type == "HumanPlayer" else "bot"

    @staticmethod
    def _human_next_move(player):
        piece_to_move = PlayerService._piece_to_move(player)
        position_to_move = PlayerService._position_to_move()

    @staticmethod
    def _piece_to_move(player):
        pass

    @staticmethod
    def _position_to_move(player):
        pass


# TODO: _piece_to_move
# TODO: _position_to_move