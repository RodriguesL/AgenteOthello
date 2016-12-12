class Minimax:
    def __init__(self, color):
        self.color = color
        self.max_depth = 4
        self.jogada = None




    def play(self, board):
        self.minimax_corte(board, self.max_depth, self.color, float('-inf'), float('inf'), True)
        return self.jogada

    def minimax_corte(self, board, depth, color, parent_alpha, parent_beta, max_gamer):
        def avaliacao(board, color ):
            peso = [
                [120, -20, 20, 5, 5, 20, -20, 120],
                [-20, -40, -5, -5, -5, -5, -40, -20],
                [20, -5, 15, 3, 3, 15, -5, 20],
                [5, -5, 3, 3, 3, 3, -5, 5],
                [5, -5, 3, 3, 3, 3, -5, 5],
                [20, -5, 15, 3, 3, 15, -5, 20],
                [-20, -40, -5, -5, -5, -5, -40, -20],
                [120, -20, 20, 5, 5, 20, -20, 120],
            ]
            estabilidade = 0
            estabilidade_oponente = 0
            for i in range(1,9):
                for j in range(1,9):
                    if board.board[i][j] == color:
                        estabilidade += peso[i-1][j-1]
                    elif board.board[i][j] == board._opponent(color):
                        estabilidade_oponente += peso[i-1][j-1]

            return estabilidade - estabilidade_oponente

        moves = board.valid_moves(color)
        pontuacao = None
        melhorJogada = None
        if depth == 0 or not moves:
            pontuacao = avaliacao(board, color)
            return pontuacao
        alpha = float('-inf')
        beta = float('inf')
        oponente = board._opponent(color)
        for move in moves:
            jogada_simulacao = board.get_clone()
            jogada_simulacao.play(move, color)
            melhorPontuacao = self.minimax_corte(jogada_simulacao, depth - 1, oponente, alpha, beta, not(max_gamer))
            if max_gamer:
                if melhorPontuacao > alpha:
                    alpha = melhorPontuacao
                    melhorJogada = move
                pontuacao = alpha
                if pontuacao > parent_beta:
                    break
            else:
                beta = min(melhorPontuacao, beta)
                pontuacao = beta
                if pontuacao < parent_alpha:
                    break
        if depth == self.max_depth:
            self.jogada = melhorJogada

        return pontuacao





