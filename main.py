# © Tokai
import requests as r
import logging
from uuid import uuid4

from telegram import InlineQueryResultAudio
from telegram.ext import Updater, InlineQueryHandler

from configs import Config
from Attach.command import start_hand, help_hand, donate_hand
from Attach.callback import main_callback


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def inline(update, context):
    query = update.inline_query
    q.query = query.query
    hasil = []
    if q.query == '':
        q.id = query.id
        context.bot.answer_inline_query(
            inline_query_id = q.id,
            results = hasil,
            switch_pm_text = 'Masukkan judul lagu!',
            switch_pm_parameter = 'help',
            cache_time = 0
        )
    else:
        try:
            jo = q.query.replace(' ','%20')
            response = r.get(f'https://api.zeks.xyz/api/joox?apikey=JIzJ6hEHEcjsojbYEjhV9nzJ82D&q={jo}').json()
            result = response.get('data')
            for x in result:
                judul = x.get('judul')
                artis = x.get('artist')
                musik = x.get('audio')
                teks_judul = '{} - {}'
                hasil.append(InlineQueryResultAudio(
                    id = uuid4(),
                    audio_url = musik,
                    title = teks_judul.format(judul, artis)
                )
            )
            update.inline_query.answer(results = hasil, cache_time = 0)
        except:
            pass

def main():
    updater = Updater(Config.BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # command dengan handler
    dispatcher.add_handler(start_hand)
    dispatcher.add_handler(help_hand)
    dispatcher.add_handler(donate_hand)

    # command tanpa handler
    dispatcher.add_handler(InlineQueryHandler(inline))
    dispatcher.add_handler(main_callback)

    # aktifkan bot
    updater.start_webhook(listen="0.0.0.0",
                          port=Config.PORT,
                          url_path=Config.BOT_TOKEN,
                          webhook_url="https://{}.herokuapp.com/{}".format(Config.APP_NAME, Config.BOT_TOKEN))
    updater.idle()

if __name__ == '__main__':
    main()
