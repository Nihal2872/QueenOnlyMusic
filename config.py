from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

ASS_HANDLER = list(getenv("ASS_HANDLER", "/").split())
BOT_TOKEN = getenv("BOT_TOKEN")


DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
LOGGER_ID = int(getenv("LOGGER_ID"))
MONGO_DB_URI = getenv("MONGO_DB_URI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "926151330").split()))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/8021f124a9a418cb61a98.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/1aced97b4bf66aa2140a9.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+qX4DpUpNzv05NTY9")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+qX4DpUpNzv05NTY9")

STRING_SESSION = getenv("STRING_SESSION", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "926151330").split()))
