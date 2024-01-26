import requests
import spotipy
import os
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# Your information
# You can get it from development dashboard
username = os.environ.get('username') # Your username
CLIENT_ID = os.environ.get('CLIENT_ID') # Your CLIENT ID
CLIENT_SECRET = os.environ.get('CLIENT_SECRET') # Your CLIENT SECRET

redirect_uri = "http://example.com"
scope = "playlist-modify-private"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Get request to hot 100 billboard
billboard_url = "https://www.billboard.com/charts/hot-100/"
response = requests.get(billboard_url + date)
response.raise_for_status()

# Scrape the top 100 song titles
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# Authentication with Spotify
# Implements Authorization Code Flow for Spotify’s OAuth implementation.
# Get current id ( Spotify username)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=redirect_uri,
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username=username))
user_id = sp.current_user()["id"]

# Create a list of Spotify song URI
year = date.split("-")[0]
song_uris = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating and adding to Spotify Playlist
playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{date} Billboard 100",
                                   public=False)
playlist_id = playlist['id']
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
