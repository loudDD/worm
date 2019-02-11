"""
https://m.duzhez.com/manhua/12730/473308.html?p=2
https://m.duzhez.com/manhua/12730/

https://m.duzhez.com/manhua/12730/473582.html
https://m.duzhez.com/manhua/12730/473859.html
https://m.duzhez.com/manhua/12730/473308.html?p=3
第一张图片url xpath //*[@id="page-1"]
第四张图片url xpath //*[@id="page-4"]

第几话//*[@id="chapter-list-1"]/li[1]/a/span
"""
import requests
from lxml import etree
import os
from selenium import webdriver
import re
from time import sleep
import threading

def zijipatu(url_info):
    """
    根据传入的url，来获得URL,总页数,以此来获取图片，并重命名
    注意传入的是一个列表，且前提每话的url和总页数元素定位方式相同
    :param url:
    :return:
    """

    for i,j in url_info.items():
        # header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"}
        page_info = requests.get(j)
        selector = etree.HTML(page_info.text)
        total_page = int(selector.xpath('//*[@id="total-page"]/text()')[0])
        # print(total_page)
        try:
            for x in range(2,total_page+1):
                param = {"p":x}
                # htmlcontent = requests.get(j,params=param)
                url =j + "?" + "p=" + str(x)
                driver = webdriver.Firefox()
                driver.get(url)
                driver.implicitly_wait(15)
                htmlcontent = driver.page_source
                # print(htmlcontent.url)
                # image_xpath = '//*[@id="page-%d"]/@src' %(x)
                # print("image_xpath:" , image_xpath)
                # selector1 = etree.HTML(htmlcontent)
                # photourl = selector1.xpath(image_xpath)
                # print("selector1: " ,selector1)
                # print("photourl:",photourl)

                basephoto = requests.get(re.findall('src=\"(.*?)"',htmlcontent)[3])
                # print("basephoto:" , basephoto)
                filepath = "D:/comic/" + i
                file = filepath + "/" + str(x) + ".jpg"
                if not os.path.exists(filepath):
                    os.makedirs(filepath)

                with open(file,"wb") as f:
                    if os.path.getsize(file) < 10:
                        f.write(basephoto.content)
                    f.close()
                    driver.quit()
        except:
            raise ValueError


def geturl(comicpageurl):
    """
    从漫画根目录获取每话的根路径，以此来确定每话的url和总页数
    :param comicpageurl:
    :return:
    """
    url = {}
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2864.400"}
    urllist = requests.get(comicpageurl,headers = header)
    selector = etree.HTML(urllist.text)
    numlist = selector.xpath ('//*[@id="chapter-list-1"]/li/a/span/text()')
    # print(numlist)
    hreflist = selector.xpath('//*[@id="chapter-list-1"]/li/a/@href')
    # print(hreflist)
    for x,y in zip(hreflist,numlist):
        url[y]= "https://m.duzhez.com" + x
    # print(url)
    return  url
comicpageurl = "https://m.duzhez.com/manhua/12730/"

url_info = geturl(comicpageurl)

zijipatu(url_info)
