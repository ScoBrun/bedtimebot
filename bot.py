import logging
import time
from bot_token import BOT_TOKEN_ID

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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

def handler_sleepnow(update, context):
    """
    TODO

    Arguments:
        update {object} -- telegram bot updater object
        context {object} -- input context object
    """

def handler_sleepat(update, context):
    """
    TODO

    Arguments:
        update {object} -- telegram bot updater object
        context {object} -- input context object
    """
	
def handler_wakeupat(update, context):
    """
    TODO

    Arguments:
        update {object} -- telegram bot updater object
        context {object} -- input context object
    """
	
def handler_help(update, context):
    """
    TODO

    Arguments:
        update {object} -- telegram bot updater object
        context {object} -- input context object
    """

def handler_github(update, context):
    """
    TODO

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
