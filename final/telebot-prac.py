import secret
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

updater = Updater(token=secret.access_token, use_context=True)
dispatcher = updater.dispatcher

'''
def init(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='參考資料', reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                '課程 E3', url='https://e3.nycu.edu.tw/course/view.php?id=23863'),
            InlineKeyboardButton(
                '課程 Github', url='https://github.com/mzshieh/pa21spring')
        ], [InlineKeyboardButton(
            'Python Telegram Bot 文件', url='https://python-telegram-bot.readthedocs.io/en/stable/index.html'),
            InlineKeyboardButton('國立陽明交通大學', url='https://www.nycu.edu.tw/')
        ]])
    )
'''


def init(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='參考資料', reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('功能 A', callback_data='a'),
            InlineKeyboardButton('功能 B', callback_data='b')
        ], [InlineKeyboardButton('功能 C', callback_data='c')]])
    )


def func(update, context):
    if update.callback_query.data == 'a':
        context.bot.answer_callback_query(update.callback_query.id, '你按的是功能 A')
    elif update.callback_query.data == 'b':
        context.bot.edit_message_text('你按的是功能 B', chat_id=update.callback_query.message.chat_id,
                                      message_id=update.callback_query.message.message_id)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="你按的是功能 C")


start_handler = CommandHandler('start', init)
dispatcher.add_handler(CallbackQueryHandler(func))
dispatcher.add_handler(start_handler)

updater.start_polling()