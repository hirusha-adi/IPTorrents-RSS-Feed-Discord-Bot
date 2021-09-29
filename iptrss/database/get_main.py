import json

class BotMain:

    with open("iptrss/database/main.json", "r", encoding="utf8") as embedsf:
        embeddata = json.load(embedsf)

    MSG_PREFIX = embeddata["MSG_PREFIX"]
    BOT_VERSION = embeddata["BOT_VERSION"]
    CREATOR_NAME = embeddata["CREATOR_NAME"]
    TOKEN = embeddata["TOKEN"]


