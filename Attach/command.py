# © Tokai
import logging

from configs import Config
from telegram import(
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ParseMode,
    Chat,
    ChatAction
)
from telegram.ext import CommandHandler

logger = logging.getLogger(__name__)

def start_command(update, context):
    msg = update.effective_message
    context.bot.send_chat_action(
        chat_id=msg.chat_id,
        action=ChatAction.TYPING
    )
    usr = update.effective_user.first_name
    chat = update.effective_chat
    if chat.type == 'private':
        context.bot.send_message(
            chat_id=msg.chat_id,
            text=Config.START_TEXT.format(usr, context.bot.first_name),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
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
        )
    elif chat.type in [Chat.GROUP, Chat.SUPERGROUP]:
        context.bot.send_message(
            chat_id=msg.chat_id,
            text='_Hi, apa kabarmu? aku siap untuk mendownload musik untukmu._',
            parse_mode=ParseMode.MARKDOWN,
            reply_to_message_id=msg.message_id
        )
        
def help_command(update, context):
    msg = update.effective_message
    context.bot.send_chat_action(
        chat_id=msg.chat_id,
        action=ChatAction.TYPING
    )
    chat = update.effective_chat
    if chat.type == 'private':
        context.bot.send_message(
            chat_id=msg.chat_id,
            text=Config.HELP_TEXT,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text='About Bot 🤖',
                                             callback_data='bot_cmd'),
                        InlineKeyboardButton(text='💻 Developer',
                                             url='https://t.me/fckualot')
                    ]
                ]
            )
        )
    elif chat.type in [Chat.GROUP, Chat.SUPERGROUP]:
        context.bot.send_message(
            chat_id=msg.chat_id,
            text='_Tekan tombol dibawah untuk melihat semua perintahku!!_',
            parse_mode=ParseMode.MARKDOWN,
            reply_to_message_id=msg.message_id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text='Bantuan 📚',
                                             url='t.me/{}?start'.format(context.bot.username))
                    ]
                ]
            )
        )
    
def donate_command(update, context):
    msg = update.effective_message
    context.bot.send_chat_action(
        chat_id=msg.chat_id,
        action=ChatAction.TYPING
    )
    usr = update.effective_user.first_name
    chat = update.effective_chat
    if chat.type == 'private':
        context.bot.send_message(
            chat_id=msg.chat_id,
            text=Config.DONATE_TEXT.format(usr),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text='💵 Donasi', url='{}'.format(Config.DONATE_LINK)),
                        InlineKeyboardButton(text='Others 💶', url='t.me/{}'.format(Config.OWNER_USERNAME))
                    ]
                ]
            )
        )
    elif chat.type in [Chat.GROUP, Chat.SUPERGROUP]:
        context.bot.send_message(
            chat_id=msg.chat_id,
            text='_Maaf, donate hanya dapat dilakukan pada private chat. Tekan tombol dibawah untuk melanjutkan_',
            parse_mode=ParseMode.MARKDOWN,
            reply_to_message_id=msg.message_id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text='Donate 💵',
                                             url='t.me/{}?start'.format(context.bot.username))
                    ]
                ]
            )
        )
        
start_hand = CommandHandler('start', start_command)
help_hand = CommandHandler('help', help_command)
donate_hand = CommandHandler('donate', donate_command)
