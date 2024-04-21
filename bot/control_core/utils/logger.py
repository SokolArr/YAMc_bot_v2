# import logging
# from logging import Logger
import logging
from logging import FileHandler, Formatter
from datetime import datetime as dt

#TODO delete comments

class AppLogger():
    # def __init__(self, is_debug_mode_on: bool):
    #   self.is_debug_mode_on = is_debug_mode_on
    #   if is_debug_mode_on:
    #       logging.basicConfig(level=logging.DEBUG)
    #   else:
    #       logging.basicConfig(level=logging.INFO)

    # def get_logger(self) -> Logger:
    #   if self.is_debug_mode_on:
    #       return logging.getLogger('debug_mode')
    #   else:
    #       return logging.getLogger('main')
    def __init__(self,
                    logger_name :str = 'default',
                    filename    :str = 'bot/logs/main.log',  
                    format      :str = '%(datetime)s-%(logger_name)s-%(levelname)s: %(message)s', 
                    level       :int = logging.INFO,
                    is_debug    :bool = False
    ):      
            if is_debug:
                    print(f'{logger_name} - DEBUG MODE ON!')
                    level =  logging.DEBUG
                    
            self.logger_name = logger_name
            self.format = format
            self.is_debug = is_debug
            
            logger = logging.getLogger(logger_name)
            logger.setLevel(level)
            
            logger_handler = FileHandler(filename)
            logger_handler.setLevel(level)
            logger_handler.setFormatter(Formatter(format))
            
            logger.addHandler(logger_handler)
            self.logger = logger
            
            
    def console_log(self, message: str, levelname: str):
            print(self.format % {'datetime': dt.now(), 'logger_name': self.logger_name, 'levelname': levelname, 'message': message})
            
    async def info(self, message: str):
            levelname = 'INFO'
            try:
                    self.console_log(message, levelname)
                    self.logger.info(message, extra={'datetime': dt.now(), 'logger_name': self.logger_name})
                    
            except Exception as e:
                    print(f'ERROR TO LOG: "{e}"')
                    
    async def error(self, message: str):
            levelname = 'ERROR'
            try:
                    self.console_log(message, levelname)
                    self.logger.error(message, extra={'datetime': dt.now(), 'logger_name': self.logger_name})
                    
            except Exception as e:
                    print(f'ERROR TO LOG: "{e}"')
                    
    async def debug(self, message: str):
            if self.is_debug:
                    levelname = 'DEBUG'
                    try:
                            self.console_log(message, levelname)
                            self.logger.debug(message, extra={'datetime': dt.now(), 'logger_name': self.logger_name})
                            
                    except Exception as e:
                            print(f'ERROR TO LOG: "{e}"')