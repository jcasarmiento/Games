from alphabeta import TicTacToe
from alphabeta import alpha_beta_value#,alpha_beta_value2


def play(state):
    """Makes turn and prints the result of it until the game is over
    :param state: The initial state of the game (TicTacToe)
    """
    # print(state.is_end_state())
    while not state.is_end_state():   #while the game is still going ("?" still on the board)
        if state.is_max_node():
            print("X's turn:")
            best_value=-10
            max_nd=True
        else:
            print("O's turn:")
            best_value=10
            max_nd=False

        best_move=None
        # print(best_move)
        possible_moves=state.generate_children()
        # print(possible_moves)
        for move in possible_moves:
            # print("possible move: \n",move)
            value=alpha_beta_value(move)
            # print("value: ",value)
            if max_nd:
                if value>best_value:
                    best_value,best_move=value,move
            else:
                if value<best_value:
                    best_value,best_move=value,move
        state=best_move

        print(state)


def main():
    """
    You need to implement the following functions/methods:
    play(state): makes turn and prints the result of it until the game is over
    value() in TicTacToe class: returns the current score of the game
    generate_children() in TicTacToe class: returns a list of all possible states after this turn
    alpha_beta_value(node): implements the MinMax algorithm with alpha-beta pruning
    max_value(node, alpha, beta): implements the MinMax algorithm with alpha-beta pruning
    min_value(node, alpha, beta):implements the MinMax algorithm with alpha-beta pruning
    """
    empty_board = 3 * '???'
    state = TicTacToe(empty_board, True)
    print("Original board")
    print(state)
    play(state)


if __name__ == '__main__':
    main()
