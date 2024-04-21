import requests
from datetime import datetime as dt

class Playlist():
    def __init__(self, ya_token, ya_usr_id):
        self.ya_token = ya_token
        self.ya_usr_id = ya_usr_id
        
    async def create(self, title = 'default_' + str(dt.now()), visibility = 'public') -> str:
        base_api_url = 'https://api.music.yandex.net'
        req = '/users/'+ self.ya_usr_id + '/playlists/create'
        try: #TODO rework this
            response = await requests.post(base_api_url + req, 
                                    headers = {'Authorization': 'OAuth ' + self.ya_token}, 
                                    data    = {'title': title,
                                                'visibility': visibility}
                                    ).json()
            if response['result']:
                return str(response['result']['kind'])
            else:
                return 'no res'
        except Exception as e:
            raise e
            return ''