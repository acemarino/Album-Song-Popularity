from bs4 import BeautifulSoup
import requests
import re
import json
import html
import html5lib
from selenium import webdriver
import pandas as pd


#url = 'https://music.youtube.com/browse/VLPLpbfaEmqGaklw4qglv5qA7vyxff4QLgrc'
#headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
#response = requests.get(url, headers=headers)
#content = BeautifulSoup(response.content, "html5lib")
#response.read().decode('utf-8', 'ignore')
#print(content.decode(pretty_print=True))

driver=webdriver.Chrome()
driver.get('https://music.youtube.com/browse/VLPLpbfaEmqGaklw4qglv5qA7vyxff4QLgrc')


SongArr=[]
num=1
#for song in content.find_all('a'):
    #print(song)
    #songObject = {
    #    "song": "input" 
    #}
    #num=num+1
    #SongArr.append(songObject)
#with open('songData.json', 'w') as outfile:
    #json.dump(SongArr, outfile)
    