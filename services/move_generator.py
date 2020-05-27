from services.gameboard_service import GameboardService
from services.state_checker import StateChecker
from modules.piece import Piece
from data_structures.tree import TreeNode
from copy import deepcopy


class MoveGenerator(object):

    @staticmethod
    def generate_possible_moves(node):
        valid_moves = MoveGenerator._get_valid_moves(node)
        for position in valid_moves:
            node = MoveGenerator._add_move_to_node(node, position)

        return node



    @staticmethod
    def _get_valid_moves(node):
        mode = node.data[2]
        player_color = node.data[1]
        gbstate = node.data[0]
        rows = GameboardService().get_max_rows()
        columns = GameboardService().get_max_columns()
        valid_moves = list()

        for row in range(rows):
            for column in range(columns):
                position = gbstate[row][column]
                if MoveGenerator._valid_move(position, mode, player_color):
                    valid_moves.append(position)

        return valid_moves

    @staticmethod
    def _valid_move(position, mode, player_color):
        if mode == "INIT":
            if position.piece == 'o':
                return True

        elif mode == "MOVE":
            pass

        elif mode == "FLY":
            pass

        elif mode == "MILL":
            pass


    @staticmethod
    def _add_move_to_node(node, position):
        mode = node.data[2]
        player_color = node.data[1]
        gbstate = deepcopy(node.data[0])

        if mode == "INIT":
            node.children.append(MoveGenerator._init_node(mode, player_color, gbstate, position))

        return node

    @staticmethod
    def _init_node(mode, player_color, gbstate, position):
        row = position.row
        column = position.column
        gbstate[row][column].piece = Piece(player_color)
        gbstate[row][column].piece.position = gbstate[row][column]
        new_node_data = [gbstate, player_color, mode]
        return TreeNode(new_node_data)


