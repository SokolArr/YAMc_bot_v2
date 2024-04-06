from aiogram import Bot, Dispatcher

async def main_poller(global_tg_settings, bot: Bot, dp: Dispatcher, logger, debug_logger_handler_wrapper = None):
        try:
            if debug_logger_handler_wrapper:
                dp.message.register(debug_logger_handler_wrapper.debug_handler)
        
            await logger.info(f'Bot start!')
            await bot.send_message(global_tg_settings.tg_admin_id, f'Bot start!')
            await dp.start_polling(bot)
        
        except Exception:
            raise Exception
              
        finally:
            await logger.info(f'Bot down!')
            await bot.send_message(global_tg_settings.tg_admin_id, f'Bot down!')
            await bot.session.close()
            
        