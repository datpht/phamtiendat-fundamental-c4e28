from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
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
    dic = {"song":song,"artist":artist}
    music_list.append(dic)
pyexcel.save_as(records=music_list, dest_file_name="apple_itune.xlsx")


