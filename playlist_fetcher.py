import urllib.request
from bs4 import BeautifulSoup
import re

def get_playlist_songs(link):
    # link example: "https://hospitalrecords.podbean.com/e/makoto-solah-lxt-hospital-podcast-with-degs-461/"
    page = urllib.request.urlopen(link)
    soup = BeautifulSoup(page, "html.parser")

    songs = soup.find_all("br")[1]

    return [song for song in songs.contents if str(song)[0] != "<"]