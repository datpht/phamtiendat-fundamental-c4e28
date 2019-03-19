from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
connection = urlopen(url)

raw_data = connection.read()
html_content = raw_data.decode("utf-8")
with open("s.cafef.html","wb") as f:
    f.write(raw_data)

soup = BeautifulSoup(html_content,"html.parser") 
table = soup.find("table",id="tableContent")
td_list = table.find_all("td","b_r_c")
#tb = soup.find("table",id="tblGridData") 
#tdq_list = tb.find_all("td","h_t")

big_list = []
main_title = []
quy_4_2016 = []
quy_1_2017 = []
quy_2_2017 = []
quy_3_2017 = []
bigger_list = []

for td in td_list:
    title = td.string 
    big_list.append(title)
for a in range(0,139,6):
    main_title.append(big_list[a])
for b in range(1,140,6):
    quy_4_2016.append(big_list[b])
for c in range(2,141,6):
    quy_1_2017.append(big_list[c])
for d in range(3,142,6):
    quy_2_2017.append(big_list[d])
for e in range(4,143,6):
    quy_3_2017.append(big_list[e])
for i in range(24):
    dic = {
        'danh mục':main_title[i],
        'quý 4 - 2016':quy_4_2016[i],
        'quý 1 - 2017':quy_1_2017[i],
        'quý 2 - 2017':quy_2_2017[i],
        'quý 3 - 2017':quy_3_2017[i]
    }
    bigger_list.append(dic)
#print(bigger_list)
pyexcel.save_as(records=bigger_list, dest_file_name="scafef_table.xlsx")




    





    

    

