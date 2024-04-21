class GlobalTgSettings():
    '''
        TODO: add comments
    '''
    def __init__(self, token: str, tg_admin_id: int = None, is_debug_mode_on: bool = False):
        self.token = token
        self.tg_admin_id = tg_admin_id
        self.is_debug_mode_on = is_debug_mode_on
        
    def get_settings(self):
        return self.token, self.tg_admin_id, self.is_debug_mode_on