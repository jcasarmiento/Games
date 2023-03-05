TEMPLATE_FIELD = '|e|e|e|\n|e|e|e|\n|e|e|e|\n'
HUGE_NUMBER = 1000000


class AlphaBetaNode(object):
    def __init__(self):
        pass

    def generate_children(self):
        pass

    def is_max_node(self):
        pass

    def is_end_state(self):
        pass

    def value(self):
        pass


class TicTacToe(AlphaBetaNode):
    """Class that contains current state of the game and implements AlphaBetaNode methods
    :attr state: Current state of the board (str)
    :attr state: Indicates whose turn it is (Boolean)
    """

    def __init__(self, state, crosses_turn):
        super().__init__()
        self.state = state
        self.crosses_turn = crosses_turn

    def is_end_state(self):
        return ('?' not in self.state) or self.won('x') or self.won('o')

    def won(self, c):
        triples = [self.state[0:3], self.state[3:6], self.state[6:9], self.state[::3], self.state[1::3],
                   self.state[2::3], self.state[0] + self.state[4] + self.state[8],
                   self.state[2] + self.state[4] + self.state[6]]
        combo = 3 * c
        return combo in triples

    def __str__(self):
        field = TEMPLATE_FIELD
        for c in self.state:
            field = field.replace('e', c, 1)

        return field

    def is_max_node(self):
        return self.crosses_turn

    def generate_children(self):
        """
        Generates list of all possible states after this turn
        :return: list of TicTacToe objects
        """
        children=[]
        new_turn=not self.crosses_turn
        for i in range(len(self.state)):
            # print("i(generate_children):",i)
            new_state=self.state
            if new_state[i]=='?':
                new_state=new_state[:i]+('x' if self.crosses_turn else 'o') + new_state[i+1:]
                children.append(TicTacToe(new_state,new_turn))
        return children

    def value(self):
        """
        Current score of the game (0, 1, -1)
        :return: int
        """
        if self.won('x'):
            return 1
        elif self.won('o'):
            return -1
        else:
            return 0


def alpha_beta_value(node):
    """Implements the MinMax algorithm with alpha-beta pruning
    :param node: State of the game (TicTacToe)
    :return: int
    """
    if node.is_max_node():
        return max_value(node,-HUGE_NUMBER,HUGE_NUMBER)#[0]
    else:
        return min_value(node,-HUGE_NUMBER,HUGE_NUMBER)#[0]


def max_value(node, alpha, beta):
    if node.is_end_state():
        return node.value()
    
    v=-HUGE_NUMBER

    for child in node.generate_children():
        v=max(v,min_value(child,alpha,beta))
        alpha=max(alpha,v)
        if alpha>=beta:
            return v
        
    return v


def min_value(node, alpha, beta):
    if node.is_end_state():
        return node.value()
    
    v=HUGE_NUMBER

    for child in node.generate_children():
        v=min(v,max_value(child,alpha,beta))
        beta=min(beta,v)
        if alpha>=beta:
            return v

    return v
