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
            for r in range(m-1, m+2):
                for c in range(n-1, n+2):
                    if 0 <= r < R and 0 <= c < C and board[r][c] == '*':
                        board[m][n] += 1


# display board
for row in board:
    print(*row)