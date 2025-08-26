import argparse
from chess_game.game import Game
from chess_game.ai import ChessAI
from chess_game.cli import print_board, parse_move

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ai", choices=["white","black"])
    parser.add_argument("--depth", type=int, default=2)
    args = parser.parse_args()

    game = Game()
    ai = ChessAI(args.depth) if args.ai else None

    while True:
        print_board(game.board)
        if args.ai == game.turn:
            move = ai.best_move(game)
            print(f"AI plays {move}")
            game.make_move(move)
        else:
            move_str = input(f"{game.turn} move (e.g. e2e4): ")
            move = parse_move(move_str)
            if not move:
                print("Invalid format")
                continue
            if move not in game.legal_moves():
                print("Illegal move")
                continue
            game.make_move(move)

if __name__ == "__main__":
    main()
