from modules.piece import Piece

class Player(object):
    starting_pieces = 9

    def __init__(self, color: str):
        pieces = list()

        for piece in range(self.starting_pieces):
            pieces.append(Piece(color))

        self._piece_color = color
        self.unused_pieces = pieces
        self.piece_list = list()

    @property
    def pieces_left(self):
        return len(self.piece_list) + len(self.unused_pieces)

    @property
    def has_unused_pieces(self):
        return len(self.unused_pieces) != 0

    @property
    def piece_color(self):
        return self._piece_color



class HumanPlayer(Player):

    def __init__(self, color):
        super().__init__(color)
        self._type = "human"

    @property
    def type(self):
        return self._type


class BotPlayer(Player):

    def __init__(self, color):
        super().__init__(color)
        self._type = "bot"

    @property
    def type(self):
        return self._type

if __name__ == '__main__':
    h = HumanPlayer('W')
    b = BotPlayer('B')

    for i in range(Player.starting_pieces):
        bot_piece = h.unused_pieces[i]
        human_piece = b.unused_pieces[i]
        print(bot_piece, human_piece)
        assert isinstance(bot_piece, Piece) and (human_piece, Piece)


