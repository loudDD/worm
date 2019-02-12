"""
cookies本质为类似或就是字典形式，所以使用接口中的cookies需要进行转化
传入cookies，requests.get(url,headers,cookies = )

"""

import requests

def getcookie(cook):
    cookies = {}
    for item in cook.split(";"):#获取的cookies以分号隔开，以等号连接的键值对
        k,v = item.split("=",1)#一般键不含有等号，值可能含有，所以以等号split时，明确次数
        cookies[k.strip()] = v.replace('"','')#去除键前后的空格；去除值的双引号
    return  cookies


requests.get(url="",cookies = getcookie())
