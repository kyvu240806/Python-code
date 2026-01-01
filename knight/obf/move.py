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

    for move in possible_moves:
        board.squares[move[1]][move[0]] = 1
        track.append(move)

        pre_move = knight.square
        knight.square = move

        result = go_around(board, knight, track)
        if result:
            return result

        knight.square = pre_move
        track.pop()
        board.squares[move[1]][move[0]] = 0

    return None
