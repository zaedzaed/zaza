## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBTZPqOSJBnq6F3QmTPdtFBaLA4ZfawcbZeZfF86zd08AOH_KZ_-VajHEHNS9zwGHWaMjS330N_EdD5j82Qhm-_ve6xsuJLE2UwvM6cs4q60eYnRtYHulVPjgTFe5PtQur1MUc_0OvciYyATKfrM_UZ0JPzc-gNDmpkpOhHivSi787IgZiWMLTMJEZP08ijtGeSR0m9sHoGJSMaE0h2K0syv0KryrQHW3dKgBcfC1kZAhGD_z5lq7zYu5Hv8v_mYpZQMwVkoP5QZis2_YN8aIBbAGv9Gz8v12Zsh1mfMMCclf5-txgxL2lJvv75bxFTLuYvK0Vmju7tWrYrM6BuybMyAAAAAUrqj_gA")
BOT_TOKEN = getenv("BOT_TOKEN", "5432921604:AAEsET7VHSTjUJKfgwL3UGXDvCfnWYb_13s")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "F84RF")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "TiGexbot")
OWNER_ID = getenv("OWNER_ID", "5176314812")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Paaane")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "F84RF")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "F04FF")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5176314812").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/f7e1acf9338cc453a87ad.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
