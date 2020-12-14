from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = "https://www.youtube.com/playlist?list=PLIO7o3VwD0X_hglBI3zHjZQW6GOJT30Vy"
driver.get(url)

elem = driver.find_element_by_tag_name('html')

for x in range(47):
    elem.send_keys(Keys.END)
    time.sleep(5)

innerHTML = driver.execute_script("return document.body.innerHTML")

page_soup = bs(innerHTML, 'html.parser')
res = page_soup.find_all('a',{'class':'yt-simple-endpoint style-scope ytd-playlist-video-renderer'})

titles = []
for video in res:
    if video.get('href') != None:
        titles.append((video.get('href')))

f = open('newlinks3.txt','w')
for x in titles:
    f.write(x+'\n')

print(len(titles))
driver.close()
