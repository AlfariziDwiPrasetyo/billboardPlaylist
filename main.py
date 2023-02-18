from bs4 import BeautifulSoup
import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth
Client_ID = "6c288e0cfaee469e945fd32c69b82209"
Client_Secret= "bcbce8c44d1141ff99a3f688518fbd15"
redirect_URI="http://google.com"

# scrap judul lagu

time = input("Masukkan tahun dalam format YYYY-MM-DD : ")
print("Loading...")
link = f"https://www.billboard.com/charts/hot-100/{time}"
response = requests.get(link)
spo_web_page = response.text

web = BeautifulSoup(spo_web_page, "html.parser")

list_lagu = []
judul_lagu = web.select("ul li li .c-title")
for judul in judul_lagu:
    list_lagu.append(judul.text.strip())



# autentifikasi

spotify_auth = spotipy.oauth2.SpotifyOAuth(client_id=Client_ID,
client_secret=Client_Secret,
redirect_uri=redirect_URI,
scope="playlist-modify-private",
show_dialog=True,
cache_path="token.txt"
)
spotify_auth.get_access_token(as_dict=False)
s = spotipy.Spotify(oauth_manager=spotify_auth)
user_id = s.current_user()["id"]
print (user_id)
