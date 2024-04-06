# Other main imports
import asyncio
import time
from datetime import datetime as dt
from datetime import timezone as tz

# Aiogram
from aiogram import Bot, Dispatcher
from aiogram import F
from aiogram.filters.command import Command

# Settings
from settings.global_settings import GlobalTgSettings
from settings.logger_settings import AppLogger
from settings.creds import creds

# Utils
from utils.main_poller import main_poller
from utils.commands import set_commands

# Handlers
from handlers.start import start_handler
from handlers.web import WebHandlerWrapper
from handlers.debug import DebugHandlerWrapper

# Main init
global_tg_settings = GlobalTgSettings(**creds)
web_handler_wrapper = WebHandlerWrapper(global_tg_settings.web_site)
logger = AppLogger(logger_name='main_logger')

# Debug mode
if global_tg_settings.is_debug:
    debug_logger = AppLogger(logger_name='debug_logger',
                             is_debug=global_tg_settings.is_debug, 
                             filename='bot/logs/debug_logger.log')
    debug_logger_handler_wrapper = DebugHandlerWrapper(debug_logger)

# Bot init
bot = Bot(token=global_tg_settings.token)
dp = Dispatcher()
dp['bot_start_dt'] = dt.now(tz.utc)
dp.message.register(start_handler, Command("start"))
dp.message.register(web_handler_wrapper.web_handler, Command("web"))
    
# Main alive func
async def start():
    try:
        await set_commands(bot)
        await main_poller(global_tg_settings, bot, dp, logger, debug_logger_handler_wrapper)
        
    except Exception:
        raise Exception
    
if __name__ == '__main__':
    while True:
        try:
            asyncio.run(start())
            
        except Exception as e:
            logger.error(f'Bot down with error: "{e}"')
            time.sleep(5)