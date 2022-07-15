## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BABgvh10YKZIoTLX-eNEK4U7QsVFKZKfu1e8DyerQHU1YIkcpXVEFgKLvh9JtIdbMfJe4cp5wShuXawUMDCtpRkop7amgkN2xYCEMeD0t5XbUpvqDT4Z8s97m42RrerXdi8fR_YOwE8-k3EomNuEN9zuKPCx_D5NGihZxyRYEiBo7CWKuel8NIR1lGGM1CkHhkbnEflBqNMMG1Igj2ack6I8hR7uX0fP-x3ioBUR4sE73nW6WHvblxMjhmonDg9YpjbBUSfnZzCdYhh6Jv0l8hm1tWT_1YvpNxNce683K7TbT1mDU6M5xqsm_IuFYnhCuno_U2pbXtqKl4Rba-eNPvDiAAAAACbwiEIA")
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
