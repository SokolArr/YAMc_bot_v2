from aiogram import types
from datetime import datetime as dt

async def start_handler(message: types.Message, bot_start_dttm: dt):
    if message.date > bot_start_dttm:
        await message.answer(f'start_init')