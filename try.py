import re
#1、匹配一行文字中的所有开头的字母内容
s = "i love you not because of who you are, but because of who i am when i am with you"

print(re.findall('(\w)\w*\s*',s))
#2、匹配一行文字中的所有开头的数字内容
s = "i love you not because 12sd 34er 56df e4 54434"
print(re.findall(r"(\d)\d*",s))

#4、 只匹配包含字母和数字的行

s = "ilove you not because\n12sd 34er 56\ndf e4 54434"
print(re.findall(r"\w*[^\n]",s))

#5、写一个正则表达式，使其能同时识别下面所有的字符串：'bat', 'bit', 'but', 'hat', 'hit', 'hut‘

s = "'bat', 'bit', 'but', 'hat', 'hit', 'hut"
p = r"..t"

#替换邮箱
s="693152032@qq.com, werksdf@163.com, sdf@sina.com sfjsdf@139.com, soifsdfj@134.com pwoeir423@123.com"
p = r"(\w+)@\w+.com"
print(re.findall(p,s))
print(re.sub(p,"abc",s))
