from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
url = "https://www.apple.com/itunes/charts/songs/"
connect = urlopen(url)

raw_data = connect.read()
html_content = raw_data.decode("utf-8")

soup = BeautifulSoup(html_content,"html.parser")

section = soup.find("section","section chart-grid")

li_list = section.find_all("li")

music_list = []

for li in li_list:
    h3 = li.h3
    h4 = li.h4
    a = h3.a
    b = h4.a
    song = a.string
    artist = b.string
    #dic = {"song":song,"artist":artist}
    #music_list.append(dic)
    option = {
        'default_search':'ytsearch',
        'download':1
    }
    dl = YoutubeDL(option)
    dl.download([song])


   
