from .pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self.grid = self._create_starting_board()

    def _create_starting_board(self):
        g = [[None]*8 for _ in range(8)]
        # place pawns
        for i in range(8):
            g[i][1] = Pawn("black")
            g[i][6] = Pawn("white")
        # rooks
        g[0][0], g[7][0] = Rook("black"), Rook("black")
        g[0][7], g[7][7] = Rook("white"), Rook("white")
        # knights
        g[1][0], g[6][0] = Knight("black"), Knight("black")
        g[1][7], g[6][7] = Knight("white"), Knight("white")
        # bishops
        g[2][0], g[5][0] = Bishop("black"), Bishop("black")
        g[2][7], g[5][7] = Bishop("white"), Bishop("white")
        # queens
        g[3][0], g[3][7] = Queen("black"), Queen("white")
        # kings
        g[4][0], g[4][7] = King("black"), King("white")
        return g

    def in_bounds(self, pos):
        x,y = pos
        return 0 <= x < 8 and 0 <= y < 8

    def get(self, pos):
        x,y = pos
        if not self.in_bounds(pos):
            return None
        return self.grid[x][y]

    def set(self, pos, piece):
        x,y = pos
        self.grid[x][y] = piece

    def is_empty(self, pos):
        return self.in_bounds(pos) and self.get(pos) is None

    def is_friend(self, pos, color):
        p = self.get(pos)
        return p and p.color == color

    def is_enemy(self, pos, color):
        p = self.get(pos)
        return p and p.color != color

    def ray_moves(self, pos, color, directions):
        x, y = pos
        moves = []
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            while self.in_bounds((nx,ny)):
                if self.is_empty((nx,ny)):
                    moves.append((nx,ny))
                elif self.is_enemy((nx,ny), color):
                    moves.append((nx,ny))
                    break
                else:
                    break
                nx += dx; ny += dy
        return moves
