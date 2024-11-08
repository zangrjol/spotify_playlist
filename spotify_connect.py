import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import pprint
import argparse


class SpotifyConnect:
    def __init__(self):
        load_dotenv()

        self.SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
        self.SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.SPOTIFY_REDIRECT_URI = 'http://example.com'

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.SPOTIFY_CLIENT_ID,
                                                            client_secret=self.SPOTIFY_CLIENT_SECRET,
                                                            redirect_uri=self.SPOTIFY_REDIRECT_URI,
                                                            scope="playlist-modify-private playlist-modify-public",
                                                            cache_path='token.txt'))
        self.user_id = self.sp.current_user()['id']

    def find_track_uri(self, track_name):
        results = self.sp.search(q=f'track: {track_name}', type='track', limit=1)

        return results['tracks']['items'][0]['uri']

    def create_playlist(self, playlist_name):
        # Creates a playlist for a user
        self.user_id = self.sp.current_user()
        self.sp.user_playlist_create(user=self.user_id, name=playlist_name, public=False)

    def add_to_playlist(self, items_list: list):
        id = '4jUpiKpUDfOcjBKshTNVQC'
        self.sp.playlist_add_items(id, items_list)


# spotify = SpotifyConnect()
# spotify.create_playlist('Throwback Playlist')