from services.gameboard_service import GameboardService
from services.state_checker import StateChecker
from modules.piece import Piece
from data_structures.tree import TreeNode
from copy import deepcopy
from data_structures.hash_map import HashMap
from scripts.init_finishing_condition import do_players_have_unused_pieces


class MoveGenerator(object):

    @staticmethod
    def generate_possible_moves(node):
        valid_moves = MoveGenerator._get_valid_moves(node)
        for position in valid_moves:
            node = MoveGenerator._add_move_to_node(node, position)


        return node



    @staticmethod
    def _get_valid_moves(node):
        mode = node.data["mode"]
        player_color = node.data["player_color"]
        gbstate = node.data["board_state"]
        valid_moves = []

        for row in gbstate:
            for old_position in row:

                if MoveGenerator._valid_move(old_position, mode, player_color):
                    new_position = deepcopy(old_position)
                    new_piece = Piece(player_color)
                    new_piece.new_position = new_position
                    new_position.piece = new_piece
                    valid_moves.append(new_position)

        return valid_moves

    @staticmethod
    def _valid_move(position, mode, player_color):
        if mode == "INIT":
            finishing_condition = do_players_have_unused_pieces()
            if position.piece == 'o' and finishing_condition:
                return True

        elif mode == "MOVE":
            pass

        elif mode == "FLY":
            pass


    @staticmethod
    def _add_move_to_node(node, position):

        modes = {"INIT": MoveGenerator._init_node}


        mode = node.data["mode"]
        player_color = node.data["player_color"]
        gbstate = deepcopy(node.data["board_state"])


        if mode in modes:
            mill = MoveGenerator.makes_mill(gbstate, position, player_color)  # StateChecker.check_mill(gbstate, position)
            if mill:
                for oponent_position in MoveGenerator._oponents_pieces(gbstate, player_color):
                    board_copy = deepcopy(gbstate)
                    position_copy = deepcopy(position)
                    new_state = MoveGenerator._mill(mode, board_copy, oponent_position, position_copy, player_color)
                    new_node = MoveGenerator._mill_node(mode, player_color, new_state, position_copy)
                    new_node.parent = node
                    node.children.append(new_node)
            else:

                new_node = modes[mode](mode, player_color, gbstate, position)
                new_node.parent = node
                node.children.append(new_node)

        return node

    @staticmethod
    def _init_node(mode, player_color, gbstate, position):
        row = position.row
        column = position.column
        gbstate[row][column].piece = Piece(player_color)
        gbstate[row][column].piece.position = gbstate[row][column]
        new_node_data = dict() # HashMap()
        new_node_data["mode"] = mode
        new_node_data["board_state"] = gbstate
        new_node_data["player_color"] = "W" if player_color == "B" else "B"
        new_node_data["last_played_move"] = deepcopy(position)
        return TreeNode(new_node_data)

    @staticmethod
    def _mill_node(mode, player_color, gbstate, position):
        new_node_data = dict() # HashMap()
        new_node_data["mode"] = mode
        new_node_data["board_state"] = gbstate
        new_node_data["player_color"] = "W" if player_color == "B" else "B"
        new_node_data["last_played_move"] = position
        return TreeNode(new_node_data)


    @staticmethod
    def _oponents_pieces(board_state, player_color):
        oponent_color = "W" if player_color == "B" else "B"
        rows = range(len(board_state))
        columns = range(len(board_state[0]))
        oponent_pieces_positions = []
        for row in rows:
            for column in columns:
                if board_state[row][column].piece == oponent_color:
                    oponent_pieces_positions.append((row, column))

        return oponent_pieces_positions

    @staticmethod
    def _mill(mode, board_state, oponent_position, position, player_color):
        modes = {"INIT": MoveGenerator._init_mill,
                 "MOVE": None,
                 "FLY": None}

        return modes[mode](board_state, oponent_position, position, player_color)


    @staticmethod
    def _init_mill(board_state, oponent_position, position, player_color):
        place_row = position.row
        place_column = position.column
        remove_row = oponent_position[0]
        remove_column = oponent_position[1]
        empty_position = "o"

        piece_to_place = Piece(player_color)

        piece_to_place.position = board_state[place_row][place_column]
        board_state[place_row][place_column].piece = piece_to_place

        board_state[remove_row][remove_column].piece = empty_position

        return board_state














    #  Method below is too similar to to StateChecker.check_mills, so it maybe redundant
    #  A horrid method is below, please don't look at it :(
    @staticmethod
    def makes_mill(board_state, position, player_color):
        row = position.row
        column = position.column

        opposite = {"up": "down", "left": "right",
                    "down": "up", "right": "left"}

        pos = board_state[row][column]
        pos_type = pos.position_type()

        if pos_type == "connecting":
            for direction in pos.next.keys():
                if pos.has(direction):
                    if pos.next[direction].piece == player_color and \
                    pos.next[opposite[direction]].piece == player_color:
                        return True

        elif pos_type == "corner":
            for direction in pos.next.keys():
                if pos.has(direction):
                    adjacent = pos.next[direction]
                    next_in_direction = adjacent.next[direction]
                    if adjacent.piece == player_color and next_in_direction.piece == player_color:
                        return True

        elif pos_type == "border":
            direction_axis = {"horizontal": 0, "vertical": 0}
            for direction in pos.next.keys():
                if pos.has(direction):
                    if direction == "up" or direction == "down":
                        direction_axis["vertical"] += 1
                    elif direction == "left" or direction == "right":
                        direction_axis["horizontal"] += 1

            for axis in direction_axis.keys():
                if direction_axis[axis] == 2:
                    if axis == "horizontal":
                        if pos.has_left and pos.has_right:
                            if pos.left.piece == player_color and pos.right.piece == player_color:
                                return True

                    elif pos.has_up and pos.has_down:
                        if pos.up.piece == player_color and pos.down.piece == player_color:
                            return True

                elif direction_axis[axis] == 1:
                    if axis == "horizontal":
                        if pos.has_right:
                            if pos.right.piece == player_color and pos.right.right.piece == player_color:
                                return True

                        elif pos.left.piece == player_color and pos.left.left.piece == player_color:
                            return True

                    else:
                        if pos.has_up:
                            if pos.up.piece == player_color and pos.up.up.piece == player_color:
                                return True

                        elif pos.down.piece == player_color and pos.down.down.piece == player_color:
                            return True

        return False
