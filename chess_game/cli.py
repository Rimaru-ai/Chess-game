def print_board(board):
    for y in range(7,-1,-1):
        row = []
        for x in range(8):
            piece = board.get((x,y))
            row.append(piece.symbol() if piece else ".")
        print(y+1, " ".join(row))
    print("  a b c d e f g h\n")

def parse_move(move_str):
    # format: e2e4
    files = "abcdefgh"
    try:
        fx, fy, tx, ty = files.index(move_str[0]), int(move_str[1])-1, \
                         files.index(move_str[2]), int(move_str[3])-1
        return (fx,fy),(tx,ty)
    except:
        return None
