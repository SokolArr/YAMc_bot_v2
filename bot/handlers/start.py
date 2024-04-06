from aiogram import Bot
from aiogram import types
from datetime import datetime as dt

async def start_handler(message: types.Message, bot_start_dt: dt):
    if message.date > bot_start_dt:
        await message.answer(f'start_init')