## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQCSlEpxu3wQLy2AJxqNztEtU18QZ2nRWbfzvbSRYo0DKWdHmUCKtgGufUMBUUDpqll0BPX0S8b8YVHbEgEPYCcIJ5cb_KbisPKax7eTgDXlcZ1abnN9z3Paq72fH2ZsSBpvX3GNRqXO2hO2OhqH2WbuXe51wjlODgv5-Xbmhkc7rW5xtchJBJaovhx5Vgznu7ZBgYyRQHJdW4dgypQrbLFSShDJFrcp1CNuvS1-UTiYtFD_LxFxeEmjBPW3zBhH6Gg50wolF1NJ9nEv5M4yj_dJ6M8uRXRutKybtD9ydu4X1QzsUlioJxIrHw900dp-aXxk9VS0D63xMOSkXcZjsPENAAAAAUxBASYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5451443239:AAHzNL7iQgoheaVONUvuHhf2OMQvJQ9hRvM")
BOT_NAME = getenv("BOT_NAME", "ميوزك")
API_ID = int(getenv("API_ID", "11121781"))
API_HASH = getenv("API_HASH", "0619f44857b427e52f229ee3f3bdc698")
OWNER_NAME = getenv("OWNER_NAME", "اެࢪهِاެقہَ")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@RY_HV")
ALIVE_NAME = getenv("ALIVE_NAME", "اެࢪهِاެقہَ")
BOT_USERNAME = getenv("@V7R_Bot", "")
OWNER_ID = getenv("OWNER_ID", "5574295846")
ASSISTANT_NAME = getenv("@RY_HV", "")
GROUP_SUPPORT = getenv("@llllllIl2", "")
UPDATES_CHANNEL = getenv("@llllllIl2", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
