from aiogram import Bot
from aiogram import types
from datetime import datetime as dt

class DebugHandlerWrapper():
  def __init__(self, debug_logger):
    self.debug_logger = debug_logger
      
  async def debug_handler(self, message: types.Message,  bot_start_dt: dt):
    if message.date > bot_start_dt:
      try:
        await self.debug_logger.debug(f'{message}')
        
      except Exception:
        raise Exception
      