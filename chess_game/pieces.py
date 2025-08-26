class Piece:
    def __init__(self, color):
        self.color = color

    def symbol(self):
        raise NotImplementedError

    def moves(self, pos, board):
        raise NotImplementedError


class Pawn(Piece):
    def symbol(self):
        return "P" if self.color == "white" else "p"

    def moves(self, pos, board):
        moves = []
        x, y = pos
        direction = -1 if self.color == "white" else 1
        start_row = 6 if self.color == "white" else 1

        # forward move
        if board.is_empty((x, y + direction)):
            moves.append((x, y + direction))
            if y == start_row and board.is_empty((x, y + 2 * direction)):
                moves.append((x, y + 2 * direction))

        # captures
        for dx in [-1, 1]:
            nx, ny = x + dx, y + direction
            if board.is_enemy((nx, ny), self.color):
                moves.append((nx, ny))
        return moves


class Rook(Piece):
    def symbol(self):
        return "R" if self.color == "white" else "r"

    def moves(self, pos, board):
        return board.ray_moves(pos, self.color, [(1,0),(-1,0),(0,1),(0,-1)])


class Bishop(Piece):
    def symbol(self):
        return "B" if self.color == "white" else "b"

    def moves(self, pos, board):
        return board.ray_moves(pos, self.color, [(1,1),(-1,1),(1,-1),(-1,-1)])


class Queen(Piece):
    def symbol(self):
        return "Q" if self.color == "white" else "q"

    def moves(self, pos, board):
        return board.ray_moves(pos, self.color,
            [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)])


class Knight(Piece):
    def symbol(self):
        return "N" if self.color == "white" else "n"

    def moves(self, pos, board):
        x, y = pos
        deltas = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        moves = []
        for dx, dy in deltas:
            nx, ny = x+dx, y+dy
            if board.in_bounds((nx,ny)) and not board.is_friend((nx,ny), self.color):
                moves.append((nx,ny))
        return moves


class King(Piece):
    def symbol(self):
        return "K" if self.color == "white" else "k"

    def moves(self, pos, board):
        x, y = pos
        deltas = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        moves = []
        for dx,dy in deltas:
            nx, ny = x+dx, y+dy
            if board.in_bounds((nx,ny)) and not board.is_friend((nx,ny), self.color):
                moves.append((nx,ny))
        return moves
