import requests
import re
import json
import html
import html5lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://music.youtube.com/browse/VLPL6Ri1UOk51t5KtpuB5KNL9PVdSywUs_d8")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
elem = driver.find_elements_by_xpath('//yt-formatted-string[@class="title style-scope ytmusic-responsive-list-item-renderer complex-string"]')
songs=[]
for s in range(len(elem)):
    songs.append(elem[s].text)
driver.close()
with open('songData.json', 'w') as outfile:
    json.dump(songs, outfile)
    