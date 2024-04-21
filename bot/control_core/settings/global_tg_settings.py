class GlobalSettings():
    '''
        TODO: add comments
    '''
    def __init__(self, 
                tg_token: str,
                ya_token: str,
                website_url: str,
                tg_admin_id: int = None, 
                is_debug_mode_on: bool = False):
        self.tg_token = tg_token
        self.ya_token = ya_token
        self.website_url = website_url
        self.tg_admin_id = tg_admin_id
        self.is_debug_mode_on = is_debug_mode_on
        
    def get_settings(self):
        return \
        self.tg_token,\
        self.ya_token,\
        self.website_url,\
        self.tg_admin_id,\
        self.is_debug_mode_on