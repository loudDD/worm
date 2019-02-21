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
            url = {http_s.lower():http_s.lower() + "://" + ip + ":" + port}
            # print(url)
            if self.verify_proxy(url):
                proxy_list.append(self.verify_proxy(url))
                print(proxy_list)
            else:
                continue
            if len(proxy_list) > 4:
                print ("可用代理为：",proxy_list)
                return proxy_list
    def verify_proxy(self,proxy):
        try:
            print("测试代理：",proxy)
            r = requests.get(url="https://jsonip.com",proxies=proxy,timeout=3)
            # if r.status_code == 200:
            #     # return proxy
            print("        有效")
            return proxy
        except:
            print ("        无效")

if __name__ == "__main__":
    a = Scrapxici()
    a.getXiCitext(100)
# a.verify_proxy("234")

# b =requests.get(url="https://www.baidu.com",proxies={"https":"https://111.177.176.173:9999"})