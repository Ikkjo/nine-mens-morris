from modules.singleton_metaclass import Singleton


class ActivePlayer(object, metaclass=Singleton):

    def __init__(self, active_player):
        self.player = active_player

    def __str__(self):
        return str(self.player)

    @property
    def piece_color(self):
        return self.player.piece_color



# if __name__ == '__main__':
#     active = ActivePlayer("p1")
#     active.player = "p2"
#     ActivePlayer("p1")  # ne moze ovako da se promeni vrednost
#     assert str(active) == "p2"
