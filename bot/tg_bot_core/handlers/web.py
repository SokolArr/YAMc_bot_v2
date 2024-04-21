from aiogram import types
from datetime import datetime as dt

async def web_handler(message: types.Message,  bot_start_dttm: dt, website_url: str):
        if message.date > bot_start_dttm:
            markup = types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        types.InlineKeyboardButton(
                            text="Website",
                            web_app=types.WebAppInfo(url=website_url),
                        )
                    ]
                ]
            )
            await message.answer("Website", reply_markup=markup)
        else:
            return None