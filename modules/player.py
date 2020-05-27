from modules.piece import Piece
from services.state_checker import StateChecker
from services.gameboard_service import GameboardService


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

    @property
    def fly_mode(self):
        return self.pieces_left <= 3

    @property
    def number_of_pieces_in_mill(self):
        number_of_pieces_in_mill = 0
        gbstate = GameboardService().get_gameboard_state()
        for piece in self.piece_list:
            if StateChecker.is_piece_in_mill(gbstate, piece.position.row, piece.position.column):
                number_of_pieces_in_mill += 1
        return number_of_pieces_in_mill




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


