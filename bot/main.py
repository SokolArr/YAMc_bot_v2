
import asyncio
import time

from aiogram import Bot, Dispatcher
from aiogram import types as aio_types
from aiogram import F
from aiogram.filters.command import Command

from settings.global_settings import GlobalTgSettings
from settings.logger_settings import AppLogger

from settings.creds import creds

global_tg_settings = GlobalTgSettings(**creds)
logger = AppLogger(logger_name='main_logger')
if global_tg_settings.is_debug: debug_logger = AppLogger(logger_name='debug_logger', 
                                                        is_debug=global_tg_settings.is_debug, 
                                                        filename='bot/logs/debug_logger.log')

bot = Bot(token=global_tg_settings.token)
dp = Dispatcher()

async def start_handler(message: aio_types.Message):
    await message.answer(f'start_init')
    
async def all_mes_handler(message: aio_types.Message):
    await debug_logger.debug(f'{message}')
    
async def start():
    dp.message.register(start_handler, Command("start"))
    if debug_logger:dp.message.register(all_mes_handler, F.text)

    while True:
        try:
            await logger.info(f'Bot start!')
            await bot.send_message(global_tg_settings.tg_admin_id, f'Bot start!')
            await dp.start_polling(bot)
            
        except Exception as e:
            await logger.error(f'Bot down with error: "{e}"')
            await bot.send_message(global_tg_settings.tg_admin_id, f'Bot down with error: "{e}"')
            await bot.session.close()
            time.sleep(5)
            
        finally:
            await logger.info(f'Bot down!')
            await bot.send_message(global_tg_settings.tg_admin_id, f'Bot down!')
            await bot.session.close()
        
if __name__ == '__main__':
    asyncio.run(start())