import asyncio

import control_core         as cc
import database_core        as dc
import tg_bot_core          as tbc
import ya_music_api_core    as yamac

from creds import creds
tg_settings = cc.GlobalTgSettings(**creds)

bot_app = tbc.botApp(token=tg_settings.token)
logger = cc.AppLogger('main', is_debug=True)

# asyncio.run(bot_app.main(logger))
