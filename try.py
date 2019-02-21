#coding=utf-8
# import re
# #1、匹配一行文字中的所有开头的字母内容
# s = "i love you not because of who you are, but because of who i am when i am with you"

# print(re.findall('(\w)\w*\s*',s))
# #2、匹配一行文字中的所有开头的数字内容
# s = "i love you not because 12sd 34er 56df e4 54434"
# print(re.findall(r"(\d)\d*",s))

# #4、 只匹配包含字母和数字的行

# s = "ilove you not because\n12sd 34er 56\ndf e4 54434"
# print(re.findall(r"\w*[^\n]",s))

# #5、写一个正则表达式，使其能同时识别下面所有的字符串：'bat', 'bit', 'but', 'hat', 'hit', 'hut‘

# s = "'bat', 'bit', 'but', 'hat', 'hit', 'hut"
# p = r"..t"

# #替换邮箱
# s="693152032@qq.com, werksdf@163.com, sdf@sina.com sfjsdf@139.com, soifsdfj@134.com pwoeir423@123.com"
# p = r"(\w+)@\w+.com"
# print(re.findall(p,s))
# print(re.sub(p,"1abc$1",s))

# inputStr = "hello python,ni hao c,zai jian python"
# replaceStr = re.sub(r"hello (\w+),ni hao (\w+),zai jian \1", "PHP", inputStr)
# print(replaceStr)

# #sub有问题，待解决
#
# import random
# import re
# print(random.randint(1,2))
# print(round(random.random()*100))
# print(random.randrange(1,100,2))
# print(random.choice(["a","b"]))
#
#
# s = """sef,wef,sefw,fe@ ewf"""
# print(re.findall("(^s)\w+f$", s))
#
# string = "2345  3456  4567  5678"
# print(re.findall("\w+",string))
#
#
# print(string.find("4"))
#select user_id from A,B where a.user_id = b.xx_id and addtime
# import re
#
# s = "This is a test"
# b = re.findall(r"\w+",s)[::-1]
# b.reverse()
# print(b)
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import os
# option = webdriver.firefox.options.Options()
# option.add_argument("--headless")
#
# d = webdriver.Firefox(options=option)
# d.get("https://www.baidu.com")
# print(d.title)
# print(type(os.path.getsize(r"D:\comic\第1话\2.jpg")))
# print("fwfe",132)
# print("fwfe" + str(132))


# import requests
# from lxml import etree
#
# res = requests.get("https://m.duzhez.com/manhua/12730/473308.html?p=2")
# print("text:" ,res.text)
# sel = etree.HTML(res.text)
# xpa = sel.xpath('//*[@id="page-2"]/@src')
# print(xpa)

# from selenium import webdriver
#
# d = webdriver.Firefox()
# d.get("https://m.duzhez.com/manhua/12730/473308.html?p=2")
# print (d.page_source)

# import random
#
# print(random.choice("元祖，字符串，列表"))
# a = {1:13,1:23}
# for x in a.items():
#     print(x)

import requests

try:
    requests.get("https://www.baidu.com",timeout=0.0001)
except  Exception as e:
    print (e)

if None:
    print (123)