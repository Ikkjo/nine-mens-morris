from data_structures.tree import Tree, TreeNode
from algos.minimax_pruning import minimax_abp
from algos.nmm_state_eval import board_state_eval
from services.move_generator import MoveGenerator

from data_structures.hash_map import HashMap


def best_move(mode, board_state, player_color):  # Mode can be "INIT", "MILL" or "MOVE"
    depth_dict = {"INIT": 3, "MOVE": 4, "FLY": 3}

    node_data = dict()  # HashMap()
    node_data["board_state"] = board_state
    node_data["player_color"] = player_color
    node_data["mode"] = mode
    node_data["last_played_move"] = None
    root = TreeNode(node_data)

    best_next_move = minimax_abp(node=root, depth=depth_dict[mode], maximizing_player=True,
                                 evaluation_function=board_state_eval,
                                 alpha=float("-inf"), beta=float("inf"))
    row = best_next_move.last_played_move.row
    column = best_next_move.last_played_move.column
    best_move_position = (row, column)



    return best_move_position



