from functools import total_ordering
import re
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
#opens home page
driver.get("https://music.youtube.com/")

#finds search bar and clicks it
searchButton=driver.find_element_by_class_name("style-scope tp-yt-paper-icon-button")
searchButton.click()

#enters desired search term(s)
textArea=driver.find_element_by_xpath("//input[@placeholder='Search']")
artist='Wilbur'
textArea.send_keys(artist)
textArea.send_keys(Keys.RETURN)
time.sleep(3)

#finds correct artisit and clicks it
Artist=driver.find_element_by_xpath("//div[@id='contents']/ytmusic-responsive-list-item-renderer/a")
Artist.click()
time.sleep(3)

#clicks the show all for top songs on the page
showAll=driver.find_element_by_xpath("//div[@id='contents']/ytmusic-shelf-renderer/div[5]/a/tp-yt-paper-button/yt-formatted-string")
showAll.click()
time.sleep(3)

#loads all songs and then finds desired info(title,album,time)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)

#song titles
elem = driver.find_elements_by_xpath('//yt-formatted-string[@class="title style-scope ytmusic-responsive-list-item-renderer complex-string"]')
songs=[]
for s in range(len(elem)):
    songs.append(elem[s].text)
time.sleep(2)

#album title
elem = driver.find_elements_by_xpath("//div[@id='contents']/ytmusic-responsive-list-item-renderer/div[2]/div[3]/yt-formatted-string[2]/a")
albums=[]
for s in range(len(elem)):
    albums.append(elem[s].text)
time.sleep(2)

#song length
elem = driver.find_elements_by_xpath('//yt-formatted-string[@size="MUSIC_RESPONSIVE_LIST_ITEM_FIXED_COLUMN_SIZE_SMALL"]')
times=[]
for s in range(len(elem)):
    times.append(elem[s].text)
driver.close()

#creating objects that contain song name, album, and song time 
class SongObj:
    
    def __init__(self,song,album,times):
        self.song=song
        self.album=album
        self.times=times
    def __str__(self):
        return str(self.__dict__)

songObjs=[]
for i in range(len(elem)):
    newThing = SongObj(songs[i],albums[i],times[i])
    songObjs.append(newThing)
x={'song': 'Your New Boyfriend', 'album': 'Your New Boyfriend', 'times': '4:00'}
y=json.dumps(x)
print(y)
#pushing pulled data to a json file
#with open('songData.json', 'w') as outfile:
    #json.dump(songObjs[0], outfile)
    