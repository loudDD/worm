import re

with open('123.py','r',encoding="utf-8") as f:
    newdata = ""
    for line in f:
        newdata += line
        print(newdata)
    print(re.search("(^<$>)", newdata))
    newdata.replace(re.search("(^<$>)", newdata), " ")
with open("123.py","w" ,encoding="utf-8") as f:
    f.write(newdata)

# print("你好")
# with open("123.py","r",encoding='utf-8') as f:
#     for line in f:
#         print(line)
