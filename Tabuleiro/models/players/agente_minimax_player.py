from models.move import Move
SQUARE_WEIGHTS = [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0, 120, -20,  20,   5,   5,  20, -20, 120,   0,
    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
    0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0,
    0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0,
    0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0,
    0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0,
    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
    0, 120, -20,  20,   5,   5,  20, -20, 120,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
]
class Agente:

    def __init__(self, color):
        self.color = color


    def play(self, board):
        def minimax(self, board, depth, evaluate):
            def value(board):
                return -minimax(opponent(self), board, depth-1, evaluate)[0]

            if depth == 0:
                return evaluate(self, board), None

            moves = board.valid_moves(self, board)
            if not moves:
                if not any(board.valid_moves(board._opponent())):
                    return final_value(self, board)

                return value(board), None

            return max((value(Move()(m, self, list(board))), m) for m in moves)

        MAX_VALUE = sum(map(abs, SQUARE_WEIGHTS))
        MIN_VALUE = -MAX_VALUE

        def final_value(self, board):
            #
            diff = board.score(self)
            if diff < 0:
                return MIN_VALUE
            elif diff > 0:
                return MAX_VALUE
            return diff

        def minimax_searcher(depth, evaluate):
            def strategy(self, board):
                return minimax(self, board, depth, evaluate)[1]

            return strategy

        return move




