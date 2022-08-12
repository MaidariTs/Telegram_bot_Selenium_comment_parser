'''
Бот telegram.

1) 
'''

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TELEGRAM_TOKEN


class BotApp:
    _JOB_INTERVAL = 5.0

    @staticmethod
    def _get_filter_key(chat_id, user_id, phrase):
        return '%s-%s-%s' % (chat_id, user_id, phrase)

    def _load_external_chat(self):
        pass

    def _callback_check_filters(self, bot, job):
        chat_id = job.context
        found_phrases = self._get_phrases_for_user(chat_id)
        for phrase in found_phrases:
            bot.send_message(chat_id=chat_id, text=phrase)
        if len(found_phrases) > 0:
            self._send_screen(bot, chat_id)

    def _callback_start(self, bot, update, job_queue):
        bot.send_message(chat_id=update.message.chat_id, text='Welcome!')
        job_queue.run_repeating(
            self._callback_check_filters, 
            self._JOB_INTERVAL, 
            context=update.message.chat_id
        )

    def _callback_stop(self, bot, update, job_queue):
        job_queue.stop()
        bot

    def init(self):
        updater = Updater(TELEGRAM_TOKEN)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(
            CommandHandler("start", self._callback_start, pass_job_queue=True))
        dispatcher.add_handler(
            CommandHandler("stop", self._callback_stop, pass_job_queue=True))
        dispatcher.add_handler(
            CommandHandler("add-filter", self._callback_add_filter))
        dispatcher.add_handler(
            CommandHandler("show-filters", self._callback_show_filters))
        dispatcher.add_handler(
            CommandHandler("remove-filter", self._callback_remove_filter))
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    BotApp().init()