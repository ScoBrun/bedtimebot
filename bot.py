import logging

from telegram.ext import Updater, CommandHandler

import bedtimes
from bot_token import BOT_TOKEN_ID

# Debug Mode
DEBUG_MODE = False


def main():
    updater = Updater(BOT_TOKEN_ID, use_context=True)
    dispatcher = updater.dispatcher

    # Display what time to wake up at if you sleep now
    dispatcher.add_handler(CommandHandler('sleepnow', handler_sleepnow))

    # Display what time to wake if sleep at certain time
    dispatcher.add_handler(CommandHandler('sleepat', handler_sleepat))

    # Determine what time to go to bed at to take up then
    dispatcher.add_handler(CommandHandler('wakeupat', handler_wakeupat))

    # Determine what time to go to bed at to take up then
    dispatcher.add_handler(CommandHandler('help', handler_help))

    # Returns link to Github page.
    dispatcher.add_handler(CommandHandler('github', handler_github))

    updater.start_polling()
    updater.idle()


def handler_sleepnow(update):
    """
    Handler for determining when to take up at if you sleep now.

    Arguments:
        update {object} -- telegram bot updater object
        context {object} -- input context object
    """

    try:

        # Get data
        data = bedtimes.times_to_wake_up("NOW")

        # Build and return response Message
        response = f"Here are the times you should wake up at if you went to bed now:\n\n"
        for key in data:
            response += f"For {key} cycles, {data[key]}\n"
        response += "\nHave a good nights sleep!"
        update.message.reply_text(response)

    except ValueError:
        update.message.reply_text("Incorrect data format provided. Please enter a format in 24 hour time as HH:MM")


def handler_sleepat(update, context):
    """
    Handler for the times the user might want to sleep at.

    Arguments:
        update {object} -- telegram bot updater object
        context {object} -- input context object
    """

    try:

        # Get data, validate input.
        input_time = context.args.pop(0)
        if bedtimes.validate_input_time(input_time):
            data = bedtimes.times_to_sleep_at(input_time)

            # Build and return response Message
            response = f"Here are the times you should wake up at if you're sleeping at {input_time}:\n\n"
            for key in data:
                response += f"{key}, {data[key]}\n"
            response += "\nHave a good nights sleep!"
            update.message.reply_text(response)

    except ValueError:
        update.message.reply_text("Incorrect data format provided. Please enter a format in 24 hour time as HH:MM")


def handler_wakeupat(update, context):
    """
    Handler for requesting what time to wake up at.

    Arguments:
        update {object} -- telegram bot updater object
        context {object} -- input context object
    """

    try:

        # Get data, validate input.
        input_time = context.args.pop(0)
        if bedtimes.validate_input_time(input_time):
            data = bedtimes.times_to_wake_up(input_time)

            # Build and return response Message
            response = f"Here are the times you should be sleeping at if you're waking up at {input_time}:\n\n"
            for key in data:
                response += f"{key}, {data[key]}\n"
            response += "\nHave a good nights sleep!"
            update.message.reply_text(response)

    except ValueError:
        update.message.reply_text("Incorrect data format provided. Please enter a format in 24 hour time as HH:MM")


def handler_help(update, context):
    """
    Handler for providing help information to the user upon request.

    Arguments:
        update {object} -- telegram bot updater object
        context {object} -- input context object
    """


def handler_github(update, context):
    """
    Handler for providing the link to the github repo for this bot.

    Arguments:
        update {object} -- telegram bot updater object
        context {object} -- input context object
    """


if __name__ == '__main__':

    if DEBUG_MODE:
        logging.basicConfig(filename='app.log', level=logging.DEBUG,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)')
        print("Running app with debug enabled...")
        main()
    else:
        print("Running app...")
        main()
