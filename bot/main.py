import asyncio

import control_core         as cc
import database_core        as dc
import tg_bot_core          as tbc
import ya_music_api_core    as yamac

from creds import creds
settings = cc.GlobalSettings(**creds)
logger = cc.AppLogger('main', is_debug=settings.is_debug_mode_on)

bot_app = tbc.botApp(token=settings.tg_token,
                     website_url=settings.website_url
                    )

asyncio.run(bot_app.main(logger))
