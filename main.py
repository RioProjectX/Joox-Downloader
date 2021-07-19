# © Tokai
import requests as r
import logging
from uuid import uuid4

from telegram import InlineQueryResultAudio, ParseMode
from telegram.ext import Updater, InlineQueryHandler

from configs import Config
from Attach.command import start_hand, help_hand, donate_hand
from Attach.callback import main_callback


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def inline(update, context):
    query = update.inline_query.query
    jo = query.replace(' ','%20')
    hasil = []
    if query:
        response = r.get(f'https://api.zeks.xyz/api/joox?apikey=JIzJ6hEHEcjsojbYEjhV9nzJ82D&q={jo}').json()
        result = response.get('data')
        if result is not None:
            for x in result:
                judul = x.get('judul')
                artis = x.get('artist')
                musik = x.get('audio')
                teks_judul = '{} - {}'
                teks = '🎼_Powered by joox_'
                hasil.append(InlineQueryResultAudio(
                    id=uuid4(),
                    audio_url=musik,
                    title=teks_judul.format(judul, artis),
                    caption=teks,
                    parse_mode=ParseMode.MARKDOWN
                )
            )
            update.inline_query.answer(
                results=hasil,
                timeout=60,
                auto_pagination=True
            )
        else:
            print('None')
            return
    else:
        print('None')
        return

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
