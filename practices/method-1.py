# input parsing
R = int(input())
C = int(input())
k = int(input())
mine_list = []
for _ in range(k):
    m, n = [int(x) for x in input().split()]
    mine_list.append((m, n))

# board maintains the configuration of the game
# initialize the board
board = [[0] * C for _ in range(R)]
# place mines to the board
for m, n in mine_list:
    board[m-1][n-1] = '*'
# calculate the numbers on the cells without mines
for m in range(R):
    for n in range(C):
        if board[m][n] != '*':
            if 0 < m and 0 < n and board[m - 1][n - 1] == '*':
                board[m][n] += 1
            if 0 < m and board[m - 1][n] == '*':
                board[m][n] += 1
            if 0 < m and n < C - 1 and board[m - 1][n + 1] == '*':
                board[m][n] += 1
            if 0 < n and board[m][n - 1] == '*':
                board[m][n] += 1
            if n < C - 1 and board[m][n + 1] == '*':
                board[m][n] += 1
            if m < R - 1 and 0 < n and board[m + 1][n - 1] == '*':
                board[m][n] += 1
            if m < R - 1 and board[m + 1][n] == '*':
                board[m][n] += 1
            if m < R - 1 and n < C - 1 and board[m + 1][n + 1] == '*':
                board[m][n] += 1

# display board
for row in board:
    print(*row)