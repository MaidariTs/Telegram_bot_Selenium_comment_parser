'''
Бот telegram.

1) 
'''

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, 
from settings import TELEGRAM_TOKEN


class BotApp:
    def testcmd(self, )


    def init_app(self):
        updater = Updater(TELEGRAM_TOKEN)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("testcmd", testcmd))
        #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    BotApp()