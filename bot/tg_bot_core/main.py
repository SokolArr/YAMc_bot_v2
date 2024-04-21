from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.exceptions import *

from logging import Logger
from datetime import datetime as dt
from datetime import timezone as tz

import tg_bot_core.handlers as h

class botApp():
    def __init__(self, token: str, website_url: str):
        self.bot = Bot(token=token)
        
        self.dp = Dispatcher()
        self.dp['bot_start_dttm'] = dt.now(tz.utc)
        self.dp['website_url'] = website_url
        
        self.dp.message.register(h.start_handler, Command("start"))
        self.dp.message.register(h.web_handler, Command("web"))

    async def main(self, logger: Logger):
        try:
            await logger.info('BOT-START')
            await self.dp.start_polling(self.bot)
            await logger.info('BOT-DOWN')
            
        except AiogramError as e: #TODO not worked!
            print(f'ERORR: {e}')
       