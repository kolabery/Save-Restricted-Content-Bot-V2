# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "1208757"))
API_HASH = getenv("333f364ed62a7cbf57aa0cf4f507823b", "")
BOT_TOKEN = getenv("BOT_TOKEN", "7618122421:AAGnk3nq2F9zdflt3SFMUW4bDQAdvFxxLN8")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7548050316").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "-4503252335")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002288304590"))
