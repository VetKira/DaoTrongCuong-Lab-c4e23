from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel


# connect the page
url ="https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

#download page content
raw_data = conn.read()
page_content = raw_data.decode("utf8")

#find ROI 
soup = BeautifulSoup(page_content,"html.parser")
div = soup.find("div","section-content")
ul = soup.find("ul","")

#extract data
li_list = ul.find_all("li")

new_list = []

for li in li_list :
    a1 = li.h3.a
    a2 = li.h4.a
    name = a1.string
    artist = a2.string
   
    new =OrderedDict({
        "name": name,
        "artist": artist,
    })
    new_list.append(new)

#save data
pyexcel.save_as(records = new_list,dest_file_name = "itunes.xlsx")
