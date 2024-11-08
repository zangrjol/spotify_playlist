from bs4 import BeautifulSoup
import requests
from spotify_connect import SpotifyConnect

spotify = SpotifyConnect()

year = 2000

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

link = f'https://www.billboard.com/charts/hot-100/{year}-08-12/#'

response = requests.get(link, headers=header).text

soup = BeautifulSoup(response, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
song_uri = [spotify.find_track_uri(song) for song in song_names[:5]]

spotify.add_to_playlist(song_uri)



