import requests

s = requests.Session()#建立session对话，作用：跨请求使用cookies；类似建立一个请求实例，之后的所有请求都会使用第一次获取的cookies

response = s.get() #使用session对话代替requests的填写