from data_structures.tree import Tree
from algos.minimax_pruning import minimax_abp
from algos.nmm_state_eval import board_state_eval
from services.move_generator import MoveGenerator


def best_move(mode, board_state, player_color):  # Mode can be "INIT", "MILL" or "MOVE"
    depth_dict = {"INIT": 3, "MOVE": 4, "FLY": 3}

    board_tree = Tree([board_state, player_color, mode])
    board_tree.root = MoveGenerator().generate_possible_moves(board_tree.root)
    root = board_tree.root
    position = minimax_abp(node=root, depth=depth_dict[mode], maximizing_player=True,
                           evaluation_function=board_state_eval,
                           alpha=float("-inf"), beta=float("inf"),
                           mode=mode)
