#coding=utf-8
from lxml import etree
import requests

class Scrapxici():


    url = "https://www.xicidaili.com"

    header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
    ippath = "/td[2]/text()"
    portpath = "/td[3]/text()"
    http_spath= "/td[6]/text()"

    def getXiCitext(self,x):
        """
        根据传入的x，决定获取多少次ip
        :param x:
        :return:
        """
        proxy_list = []
        res = requests.get(self.url,headers = self.header)
        # print(res.status_code)
        for i in range(1,x):
            sel = etree.HTML(res.text)
            tablepath = '//*[@class="odd"]'+"["+str(i)+"]"
            ip = sel.xpath("".join((tablepath,self.ippath)))[0]
            port = sel.xpath("".join((tablepath,self.portpath)))[0]
            http_s = sel.xpath("".join((tablepath,self.http_spath)))[0]
            url = http_s.lower() + "://" + ip + ":" + port
            print(url)
            if self.verify_proxy(url):
                proxy_list.append(self.verify_proxy(url))
            if len(proxy_list) > 4:
                print (proxy_list)
    def verify_proxy(self,proxy):
        try:
            r = requests.get(url="https://jsonip.com",proxies=proxy)
            # if r.status_code == 200:
            #     # return proxy
            #     print("有效")
            return proxy
        except:
            print ("无效")


a = Scrapxici()
a.getXiCitext(50)
# a.verify_proxy("234")