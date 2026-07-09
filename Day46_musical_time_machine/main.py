import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

#year = input("Select the date you what to go back to? format like 'YYYY-MM-DD' only: ")
#URL = f"https://appbrewery.github.io/bakeboard-hot-100/{year}"
#response = requests.get(URL)
response = requests.get("https://appbrewery.github.io/bakeboard-hot-100/2026-03-07/")
year = "2026-03-07"
top_songs_site = response.text
soup = BeautifulSoup(top_songs_site,'html.parser')
list_of_songs = [title.getText() for title in soup.find_all(name="h3", class_="chart-entry__title")]
list_of_artists = [title.getText() for title in soup.find_all(name="span", class_="chart-entry__artist")]

playlist_name = f"{year} Billboard 100"
yt= YTMusic("browser.json")
playlists = yt.get_library_playlists()
playlist_id = 0
for playlist in playlists:
    if playlist["title"] == playlist_name:
        playlist_id = playlist["playlistId"]
if playlist_id == 0:
    playlist_id = yt.create_playlist(title=playlist_name,description=playlist_name,privacy_status="PRIVATE")

for index,song in enumerate(list_of_songs):
    try:
        next_song = yt.search(query=f"{list_of_artists[index]} {song}", filter="songs", limit=1)
        yt.add_playlist_items(playlist_id,[next_song[0]["videoId"]])
    except Exception as e:
        print(f"skipped {song} by {list_of_artists[index]} due to {e}")   
