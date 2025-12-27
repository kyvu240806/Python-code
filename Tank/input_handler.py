def input_handler(file):
	with open(file, "r") as file:
		lines = int(file.readline())
		line = []
		for i in range(lines):
			temp = file.readline().split()
			line.append(temp)
	return line