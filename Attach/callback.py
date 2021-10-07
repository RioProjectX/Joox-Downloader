# © Tokai
import logging

from configs import Config
from telegram import(
    ParseMode,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from telegram.ext import CallbackQueryHandler

logger = logging.getLogger(__name__)

START_KEY = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text='Bantuan 📚', callback_data='help_cmd')
        ],
        [
            InlineKeyboardButton(text='📣 Group', url='t.me/{}'.format(Config.GROUP_USERNAME)),
            InlineKeyboardButton(text='📣 Channel', url='t.me/{}'.format(Config.CHANNEL_USERNAME))
        ],
        [
            InlineKeyboardButton(text='About Bot 🤖', callback_data='bot_cmd')
        ]
    ]
)

HELP_KEY = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text='💻 Developer', url='https://t.me/fckualot'),
            InlineKeyboardButton(text='About Bot 🤖', callback_data='bot_cmd')
        ],
        [
            InlineKeyboardButton(text='🔙 Home', callback_data='start_cmd')
        ]
    ]
)

def callback_handle(update, context):
    query = update.callback_query
    data = query.data
    bot = context.bot
    query.answer(text='Loading')
    if data == 'start_cmd':
        usr = update.effective_user.first_name
        bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=Config.START_TEXT.format(usr, context.bot.first_name),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=START_KEY
        )
    elif data == 'help_cmd':
        bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=Config.HELP_TEXT,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=HELP_KEY
        )
    elif data == 'bot_cmd':
        bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=Config.BOT_TEXT,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )

main_callback = CallbackQueryHandler(callback_handle)
