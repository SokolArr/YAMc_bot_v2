from aiogram import types

async def start_handler(message: types.Message):
    await message.answer(f'start_init')