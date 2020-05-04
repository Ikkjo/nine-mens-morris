def minimax_abp(node, depth, maximizing_player, evaluation_function, alpha, beta):

    if depth == 0 or node.is_leaf():
        return evaluation_function(node)

    if maximizing_player:
        value = float('-inf')
        for child in node.children():

            value = max(value, minimax_abp(child, depth-1, False, evaluation_function, alpha, beta))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

    else: # minimizing player's (opponent's) move
        value = float('inf')
        for child in node.children():

            value = min(value, minimax_abp(child, depth-1, True, evaluation_function, alpha, beta))
            beta = min(beta, value)

            if alpha >= beta:
                break