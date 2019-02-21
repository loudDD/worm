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
import random
from ScrapXici import Scrapxici


header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}

def zijipatu(pre_url):
    #TODO:使用代理
    #TODO:webdriver获取url地址是否正确
    fail_list= []
    for i,j in pre_url.items():
        """
        i=每一话名字，做文件夹名
        j=每一话前置地址，拼接得到url
        用url得到页面信息，通过页面信息得到图片源地址
        """
        page_info = requests.get(j,headers=header)
        page_info.keep_live=False
        selector = etree.HTML(page_info.text)
        total_page = int(selector.xpath('//*[@id="total-page"]/text()')[0])
        proxies = Scrapxici().getXiCitext(20)
        for x in range(2,total_page+1):
            proxy = random.choice(proxies)
            filepath = "D:/comic/" + i
            file = filepath + "/" + str(x) + ".jpg"
            print("开始爬取：", i, "第" + str(x) + "张")
            if os.path.exists(file):
                if os.path.getsize(file) > 10:
                    print('已爬取过：', "  跳过")
                    continue
            # param = {"p": x}
            # htmlcontent = requests.get(j,params=param)
            url =j + "?" + "p=" + str(x)
            # print("    页面地址为：",url)
            try:
                op = webdriver.firefox.options.Options()
                op.add_argument("--headless")
                driver = webdriver.Firefox(options=op)
                driver.get(url)
                # print("    打开网页：",driver.title)
                driver.implicitly_wait(15)
                # print("    xpath为：",('//*[@id="page-%d"]' %(x)))
                image_url = driver.find_element_by_xpath('//*[@id="page-%d"]' %(x)).get_attribute("src")
                #("//*[@id="page-{}]").format(x)
                driver.quit()
            except:
                fail_list.append("获取源地址..."+"第" + str(x) + "张"+"失败")
                print("获取源地址...","失败")
                driver.quit()
                continue
            # print ("    图片源地址为：" , image_url)
            basephoto = requests.get(image_url,headers=header,proxies=proxy)
            basephoto.keep_live=False
            # print("basephoto:" , basephoto)
            if not os.path.exists(filepath):
                os.makedirs(filepath)
            with open(file,"wb") as f:
                if os.path.getsize(file) < 10:
                    f.write(basephoto.content)
                    print("    爬取" + i + str(x) + "完成")
                f.close()
            if os.path.getsize(file) < 10:
                print("    爬取失败，内容为空")
            else:
                print("    爬取成功")
            sleep(random.randint(1,5))

    print(fail_list)

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

