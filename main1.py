import argparse
import requests
import dotenv
from bs4 import BeautifulSoup


args = argparse.ArgumentParser("This is a programme to choose a date and select a year and will provide a playlist during that year")

args.add_argument("-d", "--date", required=True, help="Can you do this in this format: YYYY-MM-DD")
parser = args.parse_args()

url = "https://www.billboard.com/charts/south-africa-songs-hotw/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(url=url, headers=header)
html = response.text

soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify)
music = soup.select("li ul li h3", id="title-of-a-story", class_="c-title")

song_names = [song.getText().strip() for song in music]

print(song_names)