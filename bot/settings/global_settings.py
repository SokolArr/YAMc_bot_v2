class GlobalTgSettings():
    '''
    This is a global telegram settings class:\n
    self.token = token\n
    self.tg_admin_id = tg_admin_id\n
    self.is_debug = is_debug
    '''
    def __init__(self, token: str, tg_admin_id: int = None, is_debug: bool = False):
        self.token = token
        self.tg_admin_id = tg_admin_id
        self.is_debug = is_debug
        
    def get_settings(self):
        return self.token, self.tg_admin_id, self.is_debug