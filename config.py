import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MONGODB_URL = getenv("MONGODB_URL")
OWNER_NAME = getenv("OWNER_NAME")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_PHOTO = getenv("BOT_PHOTO")
DEV_PHOTO = getenv("DEV_PHOTO")
DEV_NAME = getenv("DEV_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "MusicJoker7x")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "J0KER_7x")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "ف ب غ س ك و م ا ت / ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/b6bae5ff811d6b0be0b40.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/votlx/soka")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/b6bae5ff811d6b0be0b40.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/b6bae5ff811d6b0be0b40.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/b6bae5ff811d6b0be0b40.jpg")
