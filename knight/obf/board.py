class Board:
	def __init__(self):
		board = [[0 for _ in range(8)] for _ in range(8)]
		board[0][0] = 1
		self.squares = board

	def empty_square(self, square):
		return self.squares[square[1]][square[0]] == 0