"""

请不要使用
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


header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
def zijipatu(url_info):
    #TODO:函数话
    #TODO:正则定位有问题
    """
    根据传入的url，来获得URL,总页数,以此来获取图片，并重命名
    注意传入的是一个列表，且前提每话的url和总页数元素定位方式相同
    :param url:
    :return:
    """

    for i,j in url_info.items():
        # header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"}
        page_info = requests.get(j,headers = header)
        selector = etree.HTML(page_info.text)
        total_page = int(selector.xpath('//*[@id="total-page"]/text()')[0])
        print("开始爬取：" ,i)
        print("    初始地址为：",j)
        # print(total_page)
        try:
            for x in range(2,total_page+1):
                # param = {"p":x}
                # htmlcontent = requests.get(j,params=param)
                url =j + "?" + "p=" + str(x)
                htmlcontent = requests.get(url,headers = header)
                # op = webdriver.firefox.options.Options()
                # op.add_argument("--headless")
                # driver = webdriver.Firefox(options=op)
                # driver.get(url)
                # print(url)
                # driver.implicitly_wait(15)
                # htmlcontent = driver.page_source
                print("    爬取页面地址：" , url)
                image_xpath = '//*[@id="page-%d"]/@src' %(x)
                print("    图片xpath为:" , image_xpath)
                selector1 = etree.HTML(htmlcontent.text)
                photourl = selector1.xpath(image_xpath)[0]
                # print("selector1: " ,selector1)
                print("    图片源地址为:",photourl)

                # basephoto = requests.get(re.findall('src=\"(.*?)"',htmlcontent)[3])#正则获取位置问题
                # print(re.findall('src=\"(.*?)"',htmlcontent)[3])
                # print("basephoto:" , basephoto)
                basephoto = requests.get(photourl,headers=header)
                filepath = "D:/comic/" + i
                file = filepath + "/" + str(x) + ".jpg"
                if not os.path.exists(filepath):
                    os.makedirs(filepath)
                with open(file,"wb") as f:
                    print(basephoto.text)
                    if os.path.getsize(file) < 10:
                        f.write(basephoto.content)
                        print("    爬取" + i + str(x) + "完成")
                    f.close()
                if os.path.getsize(file) < 10:
                    print("    爬取失败，内容为空")
                else:
                    print("    爬取成功")
        except:
            # driver.quit()
            continue


def geturl(comicpageurl):
    """
    从漫画根目录获取每话的根路径，以此来确定每话的url和总页数
    :param comicpageurl:
    :return:
    """
    url = {}
    urllist = requests.get(comicpageurl,headers = header)
    selector = etree.HTML(urllist.text)
    numlist = selector.xpath ('//*[@id="chapter-list-1"]/li/a/span/text()')
    # print(numlist)
    hreflist = selector.xpath('//*[@id="chapter-list-1"]/li/a/@href')
    # print(hreflist)
    for x,y in zip(hreflist,numlist):
        url[y]= "https://m.duzhez.com" + x
    print("获取的地址为:")
    for k,v in url.items():
        print(k + ":" + v)
        print()
    return  url
comicpageurl = "https://m.duzhez.com/manhua/12730/"

url_info = geturl(comicpageurl)

# print(url_info)
#
zijipatu(url_info)
