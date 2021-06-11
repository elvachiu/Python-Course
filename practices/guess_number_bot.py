from telegram.ext import Filters, Updater, CommandHandler, MessageHandler
from random import randint

with open('bot_token', 'r') as FILE:
    TOKEN = FILE.read()

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
answer = randint(0, 10)


def reset(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Reset! A new game starts!"
    )
    global answer
    answer = randint(0, 10)


def guess(update, context):
    number = update.message.text[7:].strip()
    try:
        number = int(number)
    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Please enter an integer. You have entered {number}."
        )
        return
    if 0 <= number <= 10:
        if number < answer:
            response = "Less than answer"
        elif number > answer:
            response = "More than answer"
        else:
            response = "Correct"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text = response
        )
        if number == answer:
            reset(update, context)
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="The input must be between 0 and 10."
        )


def remind(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Please use /start or /guess")


start_handler = CommandHandler('start', reset)
dispatcher.add_handler(start_handler)

guess_handler = CommandHandler('guess', guess)
dispatcher.add_handler(guess_handler)

repeat_handler = MessageHandler(Filters.text & (~Filters.command), remind)
dispatcher.add_handler(repeat_handler)

updater.start_polling()
