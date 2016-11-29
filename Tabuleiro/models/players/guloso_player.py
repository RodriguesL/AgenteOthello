class Guloso:

    def __init__(self, color):
        self.color = color

    def play(self, board):
        return self.getNextMove(board.valid_moves(self.color))

    def getNextMove(self, moves, board):
        melhorMovimento = None
        melhorPontuacao = -1
        for move in moves:
            x,y = move
            [white, black] = board.score()
            #Não tá certo, mas a lógica é essa. Precisa achar um jeito de "simular" move(x,y) sem de fato fazer a jogada e analisar as pontuações de todos os moves possíveis
            if self.color == board.WHITE:
                pontuacao = white
            else:
                pontuacao = black

            if pontuacao > melhorPontuacao:
                melhorPontuacao = pontuacao







