from obf.knight import Knight
from obf.board import Board
from obf.move import *
from out import print_tour

def main():
	board = Board()
	knight = Knight()
	track = [[0, 0]]
	solution = go_around(board, knight, track)
	'''solution = 
	[[0, 0], [1, 2], [2, 4], [3, 6], [5, 7], [7, 6], [6, 4], [7, 2], 
	[6, 0], [4, 1], [5, 3], [6, 5], [7, 7], [5, 6], [7, 5], [6, 3], 
	[7, 1], [5, 0], [6, 2], [7, 4], [5, 5], [6, 7], [4, 6], [5, 4], 
	[6, 6], [4, 5], [3, 3], [5, 2], [7, 3], [6, 1], [4, 0], [2, 1], 
	[4, 2], [3, 0], [1, 1], [0, 3], [2, 2], [0, 1], [2, 0], [3, 2], 
	[4, 4], [2, 3], [0, 4], [1, 6], [3, 7], [2, 5], [1, 7], [0, 5], 
	[1, 3], [3, 4], [1, 5], [0, 7], [2, 6], [4, 7], [3, 5], [2, 7], 
	[0, 6], [1, 4], [0, 2], [1, 0], [3, 1], [4, 3], [5, 1], [7, 0]]'''
	print_tour(solution)

if __name__ == "__main__":
	main()