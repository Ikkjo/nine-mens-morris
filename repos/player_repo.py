from modules.player import Player
from modules.singleton_metaclass import Singleton


class PlayerRepo(object, metaclass=Singleton):

    def __init__(self, player1, player2):
        self._player1 = player1
        self._player2 = player2

    def players(self):
        return [self._player1, self._player2]

    @property
    def player1(self):
        return self._player1

    @property
    def player2(self):
        return self._player2