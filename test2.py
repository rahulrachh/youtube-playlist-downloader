from bs4 import BeautifulSoup as bs
import requests

r = requests.get('https://www.youtube.com/playlist?list=PLIO7o3VwD0X_hglBI3zHjZQW6GOJT30Vy')
page = r.text
soup=bs(page,'html.parser')
res=soup.find_all('yt-formatted-string',{'class':'style-scope ytd-playlist-sidebar-primary-info-renderer'})
print(res)
# for l in res:
#     print(l.get('id'))




