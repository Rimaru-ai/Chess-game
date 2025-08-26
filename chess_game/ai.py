import math
import random

class ChessAI:
    def __init__(self, depth=2):
        self.depth = depth

    def evaluate(self, board):
        piece_values = {"P":1,"N":3,"B":3,"R":5,"Q":9,"K":0}
        val = 0
        for x in range(8):
            for y in range(8):
                p = board.get((x,y))
                if p:
                    s = p.symbol().upper()
                    v = piece_values[s]
                    val += v if p.color=="white" else -v
        return val

    def best_move(self, game):
        best = None
        best_val = -math.inf if game.turn=="white" else math.inf
        for move in game.legal_moves():
            game.make_move(move)
            val = self.minimax(game, self.depth-1, -math.inf, math.inf, game.turn=="black")
            game.undo()
            if game.turn=="white" and val>best_val:
                best_val, best = val, move
            elif game.turn=="black" and val<best_val:
                best_val, best = val, move
        return best

    def minimax(self, game, depth, alpha, beta, is_black):
        if depth==0:
            return self.evaluate(game.board)
        moves = game.legal_moves()
        if not moves:
            return self.evaluate(game.board)

        if not is_black:
            max_eval = -math.inf
            for move in moves:
                game.make_move(move)
                val = self.minimax(game, depth-1, alpha, beta, True)
                game.undo()
                max_eval = max(max_eval,val)
                alpha = max(alpha,val)
                if beta <= alpha: break
            return max_eval
        else:
            min_eval = math.inf
            for move in moves:
                game.make_move(move)
                val = self.minimax(game, depth-1, alpha, beta, False)
                game.undo()
                min_eval = min(min_eval,val)
                beta = min(beta,val)
                if beta <= alpha: break
            return min_eval
