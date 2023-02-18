from bs4 import BeautifulSoup
import spotipy
import requests

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
print(list_lagu)

