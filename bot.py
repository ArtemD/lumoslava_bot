from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv
import os
load_dotenv()



def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

updater = Updater(os.environ['TOKEN'])

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()