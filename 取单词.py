import re


s = '''hello world ha ha'''

p = re.split(" ",s)
p2 = re.split(" +",s)
print(p,p2)