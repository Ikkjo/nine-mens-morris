from modules.player import HumanPlayer, BotPlayer


def new_player(player_type: str, color: str):
    return HumanPlayer(color) if player_type == "human" else BotPlayer(color)
