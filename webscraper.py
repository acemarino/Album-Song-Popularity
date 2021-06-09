from bs4 import BeautifulSoup
import requests
import re
import json

url = 'https://music.youtube.com/browse/VLPLpbfaEmqGaklw4qglv5qA7vyxff4QLgrc'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

SongArr=[]
for song in content.findAll("a", attrs={'href': re.compile("^https://")}):
    songObject = {
        "song": "input" 
    }
    print(song.get('href'))
    SongArr.append(songObject)
with open('songData.json', 'w') as outfile:
    json.dump(SongArr, outfile)
    