from aiogram import Bot
from aiogram import types
from datetime import datetime as dt

class WebHandlerWrapper():
    def __init__(self, web_site_url) -> None:
      self.web_site_url = web_site_url

    async def web_handler(self, message: types.Message,  bot_start_dt: dt):
        if message.date > bot_start_dt:
            markup = types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        types.InlineKeyboardButton(
                            text="Website",
                            web_app=types.WebAppInfo(url=self.web_site_url),
                        )
                    ]
                ]
            )
            await message.answer("Website", reply_markup=markup)