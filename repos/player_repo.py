from modules.player import Player
from modules.singleton_metaclass import Singleton


class PlayerRepo(object, metaclass=Singleton):

    def __init__(self, *args):

        if len(args) != 2 or len(args) != 1 or len(args) != 0:
            raise SyntaxError("Argument mismatch in initialization of PlayerRepo")

        self._players = list()

        for arg in args:
            if isinstance(arg, Player) and len(args) == 2:
                self.players.append(arg)

            elif isinstance(arg, list) and len(args) == 1:
                self.players.extend(arg)

    @property
    def players(self):
        return self._players

    def add_player(self, player):

        if len(self._players) > 2:
            return False

        self._players.append(player)
        return True
