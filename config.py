import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "5366398706:AAEXjFLIlj1Z1fMhPIZibn03f5TQs8bFhs0")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 99999999999))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)  # Remember to give value in Minutes

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002551344112"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7874510376"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "uzeyir")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/RahidBot/UzeyirMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", ""
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/zikooblog")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sohbetNeptun")

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
STRING1 = getenv("STRING_SESSION", "BQEpUwIAE73QHnAYfrAD7rK6vvVDg31QappZREQKc80EDtrNgKwCBCUFsSq-ZxeQtzOpH2LDaCkVdyUogwvHiUr8kpoeCIh3vh2es0lBs-zbc_6x0iL7UQIl8nB0qgtUbHdYmpCI61y_V0rqaR01YyG0ocWqmaYnffBQISOOmMlR82FCA1NOuJqgWO1YlgFB-ZeAfnJ0Gv0X0oxSmhdtkTXbz3XzlzCwgwqppqGX60KJNJRgcxf7IE9ucW9jEW3SLow80Kvc4_e0P00ZTtpTF-kIBP392e6Mvwb3fFZeY3FU8d6cKG2TW4hWXGEJcC_DwIq1JgQhsAzaL14SdXIKjf0NO_NLdwAAAAHDBWw0AA")
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
    "START_IMG_URL", "https://telegra.ph/file/7d573b68b803bf874aaad.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/7d573b68b803bf874aaad.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/7d573b68b803bf874aaad.jpg"
STATS_IMG_URL = "https://telegra.ph/file/7d573b68b803bf874aaad.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/7d573b68b803bf874aaad.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/7d573b68b803bf874aaad.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/7d573b68b803bf874aaad.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/7d573b68b803bf874aaad.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/7d573b68b803bf874aaad.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/7d573b68b803bf874aaad.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/7d573b68b803bf874aaad.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/7d573b68b803bf874aaad.jpg"


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




