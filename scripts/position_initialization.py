from services.position_service import PositionService


def init_position_refs(state: list):
    return refs(state)


def refs(state):
    relations = init_relations_4() + init_relations_square()
    final_state = state
    for position in relations:
        final_state = make_refs(final_state, position[0], position[1])

    return final_state


def make_refs(state, pos: tuple, relations: dict):
    final_state = state
    for relation in relations.keys():
        final_state = new_ref(final_state, pos, relations[relation], relation)

    return final_state


def new_ref(state, pos, ref, relation):
    pos_row = pos[0]
    pos_col = pos[1]

    ref_row = ref[0]
    ref_col = ref[1]

    new_pos_and_ref = PositionService.make_reference(state[pos_row][pos_col], state[ref_row][ref_col], relation)

    state[pos_row][pos_col] = new_pos_and_ref[0]
    state[ref_row][ref_col] = new_pos_and_ref[1]

    return state


def init_relations_4():
    relations_1_1 = [(1, 1), {"up": (0, 1),
                              "down": (2, 1),
                              "left": (1, 0),
                              "right": (1, 2)}]

    relations_3_1 = [(3, 1), {"up": (1, 0),
                              "down": (6, 0),
                              "left": (3, 0),
                              "right": (3, 2)}]

    relations_4_1 = [(4, 1), {"up": (1, 2),
                              "down": (6, 2),
                              "left": (4, 0),
                              "right": (4, 2)}]

    relations_6_1 = [(6, 1), {"up": (5, 1),
                              "down": (7, 1),
                              "left": (6, 0),
                              "right": (6, 2)}]

    return [relations_1_1, relations_3_1, relations_4_1, relations_6_1]


def init_relations_square():
    relations_0_0 = [(0, 0), {"down": (3, 0),
                              "right": (0, 1)}]

    relations_0_2 = [(0, 2), {"down": (4, 2),
                              "left": (0, 1)}]

    relations_7_0 = [(7, 0), {"up": (3, 0),
                              "right": (7, 1)}]

    relations_7_2 = [(7, 2), {"up": (4, 2),
                              "left": (7, 1)}]

    relations_2_0 = [(2, 0), {"down": (3, 2),
                              "right": (2, 1)}]

    relations_2_2 = [(2, 2), {"down": (4, 0),
                              "left": (2, 1)}]

    relations_5_0 = [(5, 0), {"up": (3, 2),
                              "right": (5, 1)}]

    relations_5_2 = [(5, 2), {"up": (4, 0),
                              "left": (5, 1)}]

    return [relations_0_0, relations_0_2, relations_7_0, relations_7_2,
            relations_2_0, relations_2_2, relations_5_0, relations_5_2]
