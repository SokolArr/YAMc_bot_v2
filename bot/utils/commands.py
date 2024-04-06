from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='START TALK WITH YOU'
        ),
        BotCommand(
            command='help',
            description='HELP YOU WITH COMMANDS'
        ),
        BotCommand(
            command='web',
            description='START WEB APP'
        )
    ]
    await bot.set_my_commands(commands, 
                              BotCommandScopeDefault())