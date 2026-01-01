def print_tour(track):
    board = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(64):
        board[track[i][1]][track[i][0]] = i + 1

    for i in range(8):
        line = ""
        for j in range(8):
            line += str(board[i][j]) + "\t"
        print(line)