class Guloso:

    def __init__(self, color):
        self.color = color

    def play(self, board):
        return self.getNextMove(board.valid_moves(self.color), board)

    def getNextMove(self, moves, board):
        melhorMovimento = None
        melhorPontuacao = -1
        for move in moves:
            simulacao_jogada = board.get_clone()
            simulacao_jogada.play(move, self.color)
            [white, black] = simulacao_jogada.score()
            if self.color == board.WHITE:
                pontuacao_temp = white
            else:
                pontuacao_temp = black

            if pontuacao_temp > melhorPontuacao:
                melhorPontuacao = pontuacao_temp
                melhorMovimento = move

        return melhorMovimento











