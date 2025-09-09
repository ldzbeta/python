from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

SPOTIFY_CLIENT_ID = "2c407acdb90948809873d68f04ff9b9c"
SPOTIFY_SECRET="8a201ec6423b43e190802da451149a6d"

date_prompt = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date_prompt}/",headers=header)

soup = BeautifulSoup(response.text,"html.parser")
title_tags = soup.select(selector=".o-chart-results-list__item #title-of-a-story")

titles = [ tag.getText().strip() for tag in title_tags]


scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,client_id=SPOTIFY_CLIENT_ID,client_secret=SPOTIFY_SECRET,redirect_uri="https://example.com"))

user_id = sp.current_user()["id"]
# print(results)

song_uris = []
year = date_prompt[0:4]
for song in titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_response=sp.user_playlist_create(user=user_id,name=f"{date_prompt} Billboard 100",public=False)
playlist_id=playlist_response["id"]
sp.user_playlist_add_tracks(user=user_id,playlist_id=playlist_id,tracks=song_uris,position=None)