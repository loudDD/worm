# import requests
# from lxml import etree
#
# respon = requests.get("https://www.baidu.com")
# selector = etree.HTML(respon.ext)
#
# print(selector.xpath("//html"))
#

from bs4 import BeautifulSoup
import  requests
import re
reponse = (requests.get("https://www.douban.com")).text




soup = BeautifulSoup(reponse,"lxml")#返回源代码
soup.ul #页面中的ul标签所有元素
soup.ul.li#默认ul中第一个元素
soup.ul.li.a.string#第一个li标签中a标签的text
soup.a['href']#页面中第一个a标签的href属性，类似字典取值
soup.findAll("a")[1].string#满足条件的所有标签.第一个.text值
soup.findAll("a")[4].get('href')#取href属性
print(soup.findAll("a")[1]['href'])


#findAll简写soup()
soup(class_='item -0')#取class值，class_,因class是python关键字，所以要使用下划线


print(soup(class_='item -0'))

soup(class_=re.compile("item-"))
soup.ul.get_text()#获取文本，相当于lxml中 /text()

print(soup.ul.get_text)
a =  [x.strip() for x in soup.ul.get_text().split("\n") if x.strip()]
print(a)