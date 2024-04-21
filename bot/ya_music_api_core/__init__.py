try:
    from .playlist import Playlist
    print('✅ ya_music_api_core - loaded ')
    
except Exception as e:
    print(f'🚫 ya_music_api_core - not loaded: {e}')