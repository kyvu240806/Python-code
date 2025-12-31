class Knight:
	def __init__(self):
		self.square = [0, 0]

	def next_square(self, n):
		if n == 1:
			x = self.square[0] + 1
			y = self.square[1] + 2
		elif n == 2:
			x = self.square[0] + 2
			y = self.square[1] + 1
		elif n == 3:
			x = self.square[0] + 2
			y = self.square[1] - 1
		elif n == 4:
			x = self.square[0] + 1
			y = self.square[1] - 2
		elif n == 5:
			x = self.square[0] - 1
			y = self.square[1] - 2
		elif n == 6:
			x = self.square[0] - 2
			y = self.square[1] - 1
		elif n == 7:
			x = self.square[0] - 2
			y = self.square[1] + 1
		elif n == 8:
			x = self.square[0] - 1
			y = self.square[1] + 2
		return [x, y]