try:
    from .main import botApp
    print('✅ tg_bot_core - loaded ')
except Exception as e:
    print(f'🚫 tg_bot_core - not loaded: {e}')