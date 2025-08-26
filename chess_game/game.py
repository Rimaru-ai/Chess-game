from .board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "white"
        self.history = []

    def legal_moves(self):
        moves = []
        for x in range(8):
            for y in range(8):
                piece = self.board.get((x,y))
                if piece and piece.color == self.turn:
                    for nx,ny in piece.moves((x,y), self.board):
                        moves.append(((x,y),(nx,ny)))
        return moves

    def make_move(self, move):
        (x,y),(nx,ny) = move
        piece = self.board.get((x,y))
        captured = self.board.get((nx,ny))
        self.board.set((nx,ny), piece)
        self.board.set((x,y), None)
        self.history.append((move,captured))
        self.turn = "black" if self.turn=="white" else "white"

    def undo(self):
        if not self.history: return
        (x,y),(nx,ny), captured = *self.history.pop()[0], self.history[-1][1]
        piece = self.board.get((nx,ny))
        self.board.set((x,y), piece)
        self.board.set((nx,ny), captured)
        self.turn = "black" if self.turn=="white" else "white"
