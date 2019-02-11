import requests
from lxml import etree


url = "https://www.so.com"


header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"}
xpath = "//body/div[2]/header/section/nav/a/text()"

response = requests.get(url,headers=header)
xmltext = response.text
status_code = response.status_code

sel =etree.HTML(response.text)
a = sel.xpath(xpath)
print(a)




response = requests.get(url,headers = header)

sel = etree.HTML(response.text)
b = sel.xpath(xpath)
sel.xpath("//li[starts-with(@class,'item-')]/a/text()")#范围取值，使用相似的属相，如都已xxx开头
print(b)
sel.xpath("String(//ul)")#ul下所有文本，默认只是ul中文本，而不包括li中文本