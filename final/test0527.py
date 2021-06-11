import random


def init_board():
    global board
    global revealed
    board = [[0] * C for i in range(R)]
    revealed = [[False] * C for i in range(R)]
    mines = random.sample([(x, y) for x in range(R) for y in range(C)], k)  # 從population中取k個
    for x, y in mines:  # count the number of bombs around for every spot
        board[x][y] = '*'
        for X in range(x - 1, x + 2):
            for Y in range(y - 1, y + 2):
                if 0 <= X < R and 0 <= Y < C and board[X][Y] != '*':
                    board[X][Y] += 1


def show_board():
    for board_row, revealed_row in zip(board, revealed):
        columns = [board_row[i] if revealed_row[i] else '@' for i in range(C)]  # @ as unrevealed
        print(*columns)


def reveal_board():  # reveal the whole board when the game is over
    for board_row, revealed_row in zip(board, revealed):
        columns = [board_row[i] for i in range(C)]
        print(*columns)


def update_board(m, n):
    if m < 0 or m >= R or n < 0 or n >= C:  # out of the board
        return
    if revealed[m][n]:  # the spot has already been revealed
        return
    if board[m][n] != '*':  # reveal the spot if it is not a bomb
        revealed[m][n] = True
    if board[m][n] == 0:
        board[m][n] = '+'  # if the spot has 0 bomb around it, revealed as +
        for X in range(m - 1, m + 2):
            for Y in range(n - 1, n + 2):
                update_board(X, Y)  # recursive
    global flag  # flag = 1 -> win
    flag = 1
    for y in range(C):  # check whether there is any spot left that has no bomb
        for x in range(R):
            if revealed[x][y]:
                continue
            elif board[x][y] != '*':
                flag = 0
                break


started = False
R, C, k = 8, 9, 10  # default board
init_board()
game_over = 0

while True:
    if game_over:
        break  # game over, stop the loop
    cmd = input()
    if cmd.startswith('/start'):
        # to be implemented
        tokens = cmd.split()
        if cmd == '/start':
            R, C, k = 8, 9, 10
        elif len(tokens) == 4 and tokens[0] == '/start' and all(x.isdigit() for x in tokens[1:]):  # eg: /start 10 10 9
            if int(tokens[3]) > int(tokens[2]) * int(tokens[1]):
                print('Too many bombs')
                tokens[3] = int(tokens[2]) * int(tokens[1]) * 0.8
            R, C, k = [int(x) for x in tokens[1:]]
            if R < 8 or R > 15 or C < 8 or C > 15 or k < 0 or k > R * C:
                R, C, k = 8, 9, 10
                print('Unsupported command:', cmd)
        else:
            R, C, k = 8, 9, 10  # default
            print('Unsupported command:', cmd)
        init_board()
        reveal_board()
        started = True
    elif cmd.startswith('/open'):
        # to be implemented
        if not started:
            print('The game is not started. Input "/start" to play. ')
            continue
        try:
            tokens = cmd.split()
            loc = cmd.split("(")[1].split(")")[0].split()
            r = int(loc[0].split(',')[0])
            c = int(loc[1])
            # r, c = eval(cmd[6:])
            if len(tokens) == 3 and tokens[0] == '/open':  # eg: /open (3, 4) (m.isdigit() and n.isdigit())
                if board[r - 1][c - 1] == '*':  # boom
                    print('Game Over')
                    reveal_board()
                    started = False
                    game_over = 1
                update_board(r - 1, c - 1)
                if flag:
                    print('You win!')
                    started = False
                    game_over = 1
            else:
                print('Unsupported command:', cmd)
                continue
        except:
            print('Unsupported command:', cmd)
            continue
        if r <= 0 or r > R or c <= 0 or c > C:
            print('Unsupported command:', cmd)
            continue
    elif cmd.startswith('/replay'):
        # to be implemented
        revealed = [[False] * C for i in range(R)]  # reset revealed to default
        started = True
    else:
        print('Unsupported command:', cmd)
    if not game_over:
        show_board()
