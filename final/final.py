# Python Application - Final Project
# 0713462 IMF11

import random
import secret
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

updater = Updater(token=secret.access_token, use_context=True)
dispatcher = updater.dispatcher


def init(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='Welcome to play the Minesweeper!', reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('遊戲玩法', callback_data='how_to_play'),
            InlineKeyboardButton('遊戲規則', callback_data='rules')
        ]])
    )


def func(update, context):
    if update.callback_query.data == 'how_to_play':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="指令\n/start: 開始遊戲\n/start R C k: 指定盤面規格\n/open (x, y): 選擇想打開的位置\n按鈕\n[重玩] 重玩這一局")
    elif update.callback_query.data == 'rules':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="規格\n-盤面大小: 8 <= R, C <= 15\n-地雷數量: 不超過總格數\n-預設: R = 8, C = 9, k = 10")
    elif update.callback_query.data == 'replay':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Replay the game!")
        global started
        started = 1
        for i in range(R):
            for j in range(C):
                revealed[i][j] = False
                if board[i][j] == '+':
                    board[i][j] = 0
        context.bot.send_message(
            chat_id=update.effective_chat.id, text='The board:\n' + show_board()
        )
    elif update.callback_query.data == 'restart':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Start a new game! Type the command to start. ")


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
    columns = []
    for board_row, revealed_row in zip(board, revealed):
        columns.append([board_row[i] if revealed_row[i] else '@' for i in range(C)])  # @ as unrevealed
    show_txt = ''
    for i in range(R):
        for j in range(C):
            if revealed[i][j]:  # if it is not '@', then need a space to be neat
                show_txt += ' ' + str(columns[i][j]) + ' '
            else:
                show_txt += str(columns[i][j]) + ' '
        show_txt += '\n'
    return show_txt


def reveal_board():  # reveal the whole board -> mainly for debugging
    columns = []
    for board_row, revealed_row in zip(board, revealed):
        columns.append([board_row[i] for i in range(C)])
    show_txt = ''
    for i in range(R):
        for j in range(C):
            show_txt += ' ' + str(board[i][j]) + ' '
        show_txt += '\n'
    return show_txt


def game_over_reveal():
    for i in range(R):  # revealed all the bombs
        for j in range(C):
            if board[i][j] == '*':
                revealed[i][j] = True
    return show_board()


def update_board(m, n):
    if m < 0 or m >= R or n < 0 or n >= C:  # out of the board
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


started = 0  # to record whether the game has started or not


def start(update, context):
    global started
    if started:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Already started a game! If not know how to play:",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton('遊戲玩法', callback_data='how_to_play'),
                InlineKeyboardButton('遊戲規則', callback_data='rules')
            ]])
        )
        return
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='Start the game!'
    )
    cmd = update.message.text
    global R, C, k
    R, C, k = 8, 9, 10  # default board
    tokens = cmd.split()
    if cmd == '/start':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Set the board with default: R=' + str(R) + ', C=' + str(C) + ', k=' + str(k)
        )
    elif len(tokens) == 4 and all(x.isdigit() for x in tokens[1:]):  # eg: /start 10 10 9
        R, C, k = [int(x) for x in tokens[1:]]
        if R < 8 or R > 15 or C < 8 or C > 15 or k < 0 or k > R * C:
            R, C, k = 8, 9, 10
            context.bot.send_message(
                chat_id=update.effective_chat.id, text='Unsupported command: ' + cmd + '. Set the board with default'
            )
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text='Set the board: R=' + str(R) + ', C=' + str(C) + ', k=' + str(k)
            )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text='Unsupported command: ' + cmd + '. Set the board with default'
        )
    init_board()
    started = 1
    # show the board
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='The board:\n' + show_board()
    )
    # reveal the board -> for debugging
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='The board:\n' + reveal_board()
    )


def open_cell(update, context):
    cmd = update.message.text
    global started
    try:
        if not started:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text='The game has not started. Type "/start" to play. '
            )
            return
        tokens = cmd.split()
        r, c = eval(cmd[6:])
        if r <= 0 or r > R or c <= 0 or c > C:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text='Unsupported command: ' + cmd + '. The spot is out of range.'
            )
        elif len(tokens) == 3:  # eg: /open (3, 4)
            if board[r - 1][c - 1] == '*':  # boom
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text='Game Over :('
                )
                # game over, reveal the board
                started = 0
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text='Reveal the board:\n' + game_over_reveal()
                )
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text="Do you want to replay the game? ",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton('重玩', callback_data='replay'),
                        InlineKeyboardButton('新遊戲', callback_data='restart')
                    ]])
                )
                return
            if revealed[r - 1][c - 1]:
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text='(' + str(r) + ', ' + str(c) + ') has already been revealed. '
                )
            else:
                update_board(r - 1, c - 1)
            # show the board
            context.bot.send_message(
                chat_id=update.effective_chat.id, text='The board:\n' + show_board()
            )
            if flag:
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text='You win!\n' + reveal_board()
                )
                started = 0
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text="Do you want to replay the game? ",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton('重玩', callback_data='replay'),
                        InlineKeyboardButton('新遊戲', callback_data='restart')
                    ]])
                )
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text='Unsupported command: ' + cmd + '. Check your command. '
            )
    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text='Unsupported command: ' + cmd
        )


hey_handler = CommandHandler('hey_bot', init)
start_handler = CommandHandler('start', start)
open_cell_handler = CommandHandler('open', open_cell)
dispatcher.add_handler(hey_handler)
dispatcher.add_handler(CallbackQueryHandler(func))
dispatcher.add_handler(start_handler)
dispatcher.add_handler(open_cell_handler)

updater.start_polling()
