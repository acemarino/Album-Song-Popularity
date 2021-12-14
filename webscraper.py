from functools import total_ordering
import re
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import jsonpickle

driver = webdriver.Chrome()
#opens home page
driver.get("https://music.youtube.com/")

#finds search bar and clicks it
searchButton=driver.find_element_by_class_name("style-scope tp-yt-paper-icon-button")
searchButton.click()

#enters desired search term(s)
textArea=driver.find_element_by_xpath("//input[@placeholder='Search']")
artist='BTS'
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
elem1 = driver.find_elements_by_xpath("//div[@id='contents']/ytmusic-responsive-list-item-renderer/div[2]/div[3]/yt-formatted-string[2]/a")
albums=[]
for s in range(len(elem1)):
    albums.append(elem1[s].text)
time.sleep(2)

#song length
elem2 = driver.find_elements_by_xpath('//yt-formatted-string[@size="MUSIC_RESPONSIVE_LIST_ITEM_FIXED_COLUMN_SIZE_SMALL"]')
times=[]
for s in range(len(elem2)):
    times.append(elem2[s].text)
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
for i in range(len(elem1)):
    newThing = SongObj(songs[i],albums[i],times[i])
    songObjs.append(newThing)

#code for sorting by album
#need to refactor to make cleaner later
UnqAlbList=[]
UnqAlbList.append(songObjs[0])

totalList=[]
totalList.append(UnqAlbList)
added=False

for i in range(1,len(songObjs)):
    for j in range(len(totalList)):
        if songObjs[i].album == totalList[j][0].album:
            totalList[j].append(songObjs[i])
            added=True
        if (added == False) and (j == (len(totalList)-1)):
            newlist=[]
            newlist.append(songObjs[i])
            totalList.append(newlist)
    added=False

#pushing pulled data to a json file
with open('songData.json', 'w') as outfile:
    tester= jsonpickle.encode(totalList,unpicklable=False)
    json.dump(tester, outfile)
    