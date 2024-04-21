try:
    from .settings.global_tg_settings import GlobalSettings
    from .utils.logger import AppLogger
    print('✅ control_core - loaded ')
    
except BaseException as e:
    print(f'🚫 control_core - not loaded: {e}')