from .board import Board
from .knight import Knight

def in_board(square):
		return 0 <= square[0] <= 7 and 0 <= square[1] <= 7

def find_possible_moves(board, knight):
	possible_moves = []

	for i in range(1, 9):
		move = knight.next_square(i)
		
		if in_board(move) and board.empty_square(move):
			possible_moves.append(move)

	return possible_moves

def go_around(board, knight, track):
    if len(track) == 64:
        return track

    possible_moves = find_possible_moves(board, knight)

    for next_sq in possible_moves:
        x, y = next_sq

        board.squares[y][x] = 1
        track.append([x, y])

        old_square = knight.square
        knight.square = [x, y]

        result = go_around(board, knight, track)
        if result:
            return result

        knight.square = old_square
        track.pop()
        board.squares[y][x] = 0

    return None
