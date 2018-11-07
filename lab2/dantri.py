from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel
#1 connect to the page
url ="https://dantri.com.vn"
conn = urlopen(url)


#2 download the page content
raw_data = conn.read()
page_content = raw_data.decode("utf8") # unicode la utf8 hay utf-8
# print(page_content)


# with open("dantri.html","wb") as f:
#     f.write(raw_data) #page_content la chu co dau nen bi loi se de raw_data và w để là wb



#3 find ROI region
soup = BeautifulSoup(page_content,"html.parser")
# print(soup.prettify()) #prettify sap xep cac the ro rang hon de nhan dien
ul = soup.find("ul","ul1 ulnew") # tao se tim the ul vs class la ul1 ulnew
#href ="",id =""
# print(ul.prettify()) # do ul lay ra tu page content nen van thua huong moi dac tinh soup cua page content nen co the xai prettify




#4 extract data
li_list = ul.find_all("li")
new_list = []
# print(li_list)

# li = li_list[0] # dung cho 1 li
for li in li_list: # dung cho tat ca li
    a = li.h4.a 
    # print(a.string) # se tu hieu la lay phan content cua a
    # print(a["href"])
    title = a.string
    link = url + a["href"]
    # print(title)
    # print(link)
    new =OrderedDict({
        "title": title,
        "link" : link
    })
    new_list.append(new) # se cong don cac li vao 1 list new_list nhuwng phai khai bao new_list =[] la 1 list
    # print(new_list)
    # print("************")


#5 save data
pyexcel.save_as(records = new_list, dest_file_name = "culua.xlsx")