from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from logging import Logger

import tg_bot_core.handlers as h

dp = Dispatcher()
dp.message.register(h.start_handler, Command("start"))

class botApp():
    def __init__(self, token: str):
        self.bot = Bot(token=token)

    async def main(self, logger: Logger):
        await logger.info('BOT-STARTED')
        await dp.start_polling(self.bot)
        await logger.info('BOT-DOWN')