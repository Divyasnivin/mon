## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BABO34px1XAcm4CErq7uGtBauQeSZXihVEJrvB-dq_ju1GjAZZzGWW08I-qBpkBTOlkYN9FQ4BAvAdAW8Lym6nj98rFS7v3CD2EIvYNvLJSk8nQU6gX58XPSibswF8ES5sfFMqan4aeqVmYADClsALwVFSMbd4OjOWPGYy4g3VUQoVRP9AY4uaSvn-3wHY55S0Xoq65xvOep0gwEkrfXOODOQZT-Y8npz5wecu-CFhgJ1zejJYUbtucTDUYwOUgOmCTRE_Q86PMJT7qNqTcxt42f0rr8qbf317qwu1IEBDD36vNTlMuTxKgxx3dv3hXe-nD92qtYgZT6TgOOudxV-8alAAAAACbwiEIA")
BOT_TOKEN = getenv("BOT_TOKEN", "5130396512:AAGZQTvxI92Z47beIoNGsV3WN4DkZyZvoH0")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "19680685"))
API_HASH = getenv("API_HASH", "35c8346d7d35af39fcc9204493970277")
OWNER_NAME = getenv("OWNER_NAME", "hadi")
OWNER_USERNAME = getenv("OWNER_USERNAME", "jbbbbf")
ALIVE_NAME = getenv("ALIVE_NAME", "hadi")
BOT_USERNAME = getenv("BOT_USERNAME", "rnn0bot")
OWNER_ID = getenv("OWNER_ID", "5049024596")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "abfm0")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "kkcet")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "kkcet")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5049024596").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Divyasnivin/mon")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
