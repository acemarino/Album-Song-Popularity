import requests
import re
import json
import html
import html5lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://music.youtube.com/")
searchButton=driver.find_element_by_class_name("style-scope tp-yt-paper-icon-button")
searchButton.click()
textArea=driver.find_element_by_xpath("//input[@placeholder='Search']")
artist='BTS'
textArea.send_keys(artist)
textArea.send_keys(Keys.RETURN)
time.sleep(3)
Artist=driver.find_element_by_xpath("//div[@id='contents']/ytmusic-responsive-list-item-renderer/a")
Artist.click()
time.sleep(3)
showAll=driver.find_element_by_xpath("//div[@id='contents']/ytmusic-shelf-renderer/div[5]/a/tp-yt-paper-button/yt-formatted-string")
showAll.click()
time.sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)
elem = driver.find_elements_by_xpath('//yt-formatted-string[@class="title style-scope ytmusic-responsive-list-item-renderer complex-string"]')
songs=[]
for s in range(len(elem)):
    songs.append(elem[s].text)
driver.close()
with open('songData.json', 'w') as outfile:
    json.dump(songs, outfile)
    