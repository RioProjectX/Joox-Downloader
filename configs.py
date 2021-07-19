# © Tokai
import os

class Config(object):
    PORT = int(os.environ.get('PORT', ''))
    APP_NAME = os.environ.get('APP_NAME', '')
    OWNER_USERNAME = os.environ.get('OWNER_USERNAME', '')
    GROUP_USERNAME = os.environ.get('GROUP_USERNAME', '')
    CHANNEL_USERNAME = os.environ.get('CHANNEL_USERNAME', '')
    DONATE_LINK = os.environ.get('DONATE_LINK', '')
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
    START_TEXT = """_Hai_ *{}*, _aku adalah_ *{}*, _Aku berfungsi untuk mendownload lagu yang kalian suka dengan menggunakan fitur inline mode. Ketuk tombol bantuan dibawah untuk melihat panduanku._"""
    BOT_TEXT = """🧑🏻‍💻 *Developer :* [Tokai](t.me/tokai)

🤖 *Nama Bot :* [Clever-Mp3](https://t.me/CleverMp3_Bot)

📝 *Bahasa : * [Python3](https://www.python.org)

📚 *Library :* [python-telegram-bot](https://python-telegram-bot.readthedocs.io/en/stable/)

_Developer masih noob. Cuma bisa membaca dokumentasi official. Support aku dengan cara donate agar layanan bot tetap hidup._"""
    HELP_TEXT = """*Semua perintah yang tersedia :*

/start - _Memulai bot_
/help - _Bantuan pada bot_
/donate - _Donasi agar bot tetap aktif_

*NOTE :* _Untuk mendownload lagu, gunakan inline. Caranya ketik username bot di grup kalian, kemudian spasi judul lagu yang kalian ingin download_"""
    DONATE_TEXT = """_Halo_ *{},* _terima kasih jika kamu ingin mensupport bot dengan cara donate, berapapun nominalnya akan sangat membantu_ 😇"""
