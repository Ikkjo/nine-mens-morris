from services.move_generator import MoveGenerator
from copy import deepcopy

def minimax_abp(node, depth, maximizing_player, evaluation_function, alpha, beta):

    best_move = BestMove(board_state=deepcopy(node.data["board_state"]), last_played_move=deepcopy(node.data["last_played_move"]))

    if depth == 0:
        player_color = node.data["player_color"]
        mode = node.data["mode"]
        best_move.value = evaluation_function(best_move, player_color, mode)

        return best_move

    if maximizing_player:
        best_move.value = float('-inf')

        node = MoveGenerator().generate_possible_moves(node)
        for child in node.children:

            child.parent = node
            best_move = minimax_abp(child, depth - 1, False, evaluation_function, alpha, beta)
            evaluated_state = best_move.value

            best_move.value = max(best_move.value, evaluated_state)
            alpha = max(alpha, best_move.value)

            if alpha >= beta:
                break

    else:  # minimizing player's (opponent's) move
        best_move.value = float('inf')

        node = MoveGenerator().generate_possible_moves(node)

        for child in node.children:

            child.parent = node

            best_move = minimax_abp(child, depth - 1, True, evaluation_function, alpha, beta)
            evaluated_state = best_move.value

            best_move.value = min(best_move.value, evaluated_state)
            beta = min(beta, best_move.value)

            if alpha >= beta:
                break

    return best_move

class BestMove(object):
    def __init__(self, board_state=None, value=None, last_played_move=None):
        self.board_state = board_state
        self.value = value
        self.last_played_move = last_played_move
