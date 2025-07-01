import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "27250435"))
API_HASH = getenv("API_HASH", "5f1b167cd671b9d05fec51c89eac17da")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7682362793:AAHHwKx9sJOvpJMELPHwZvTQvwcONcyh7IQ")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 99999999999))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)  # Remember to give value in Minutes

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002840261862"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6191141179"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "rythmmusic")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Silgimusicbot/ladymusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", ""
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/rythmmusicchat")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/rythmmusicchat")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", None))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @SessionMotherBot on Telegram
STRING1 = getenv("STRING_SESSION", "AgGfzwMAbdX0-QlvNUWlFwMR2sPGGxEAqBjABUElIs1GahN5PdaKSmaCZgmEryoWcGjWHj_PTsdJQjV1MfiOoPz3TQ4O3k__39D6Kx5rjS09FKKdTQBHcCC_MhbG8R2ICzVxgPZtCTnv9lCx2qYPyBvRg_CassIWtDZsOIdQZAhGD2-vZ9kZ0-cUDUx5jg7qHlAWYUxgWkQejMPXELMB_XzJ8ivB9ubIcD6VSe1ul_I7bjvMzpHUqJMfAiSvVoOsXZQOXhso2skNW3K_MV0VwqzsYkyilQeiYt_SV_6S9ii4xoYnTK1mO1qfmHWe7R2qymhbj4cep2hg-VgTRlAbEihZff1xFgAAAAGrMHlaAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


#  ____    _    _  ___  ___   _   __  __ _   _ ____ ___ ____   ____   ___ _____ 
# / ___|  / \  | |/ / |/ / | | | |  \/  | | | / ___|_ _/ ___| | __ ) / _ \_   _|
# \___ \ / _ \ | ' /| ' /| | | | | |\/| | | | \___ \| | |     |  _ \| | | || |  
#  ___) / ___ \| . \| . \| |_| | | |  | | |_| |___) | | |___  | |_) | |_| || |  
# |____/_/   \_\_|\_\_|\_\\___/  |_|  |_|\___/|____/___\____| |____/ \___/ |_|  
                                                                               



BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/crc5ei.jpeg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/crc5ei.jpeg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/crc5ei.jpeg"
STATS_IMG_URL = "https://files.catbox.moe/crc5ei.jpeg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/crc5ei.jpeg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/crc5ei.jpeg"
STREAM_IMG_URL = "https://files.catbox.moe/crc5ei.jpeg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/crc5ei.jpeg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/crc5ei.jpeg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/crc5ei.jpeg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/crc5ei.jpeg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/crc5ei.jpeg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

    
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)




