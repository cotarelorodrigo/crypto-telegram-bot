from telegram.ext import Updater, CommandHandler
from handler_functions import help, price
from dotenv import load_dotenv
import os
import logging

load_dotenv()  # take environment variables from .env.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
updater = Updater(token=os.environ.get('TOKEN'), use_context=True)
dispatcher = updater.dispatcher

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

price_handler = CommandHandler('price', price)
dispatcher.add_handler(price_handler)

updater.start_polling()