import re

"""
match，只查看是否以确定字符开头
其中span方法，直接返回匹配的位置
其中group，返回匹配的字符（如abcddge wef中查找\w+ is \w+）
匹配条件中”wefwef（）wefwef“括号内内容为要取出的内容
"""

text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

print(re.match("Beauti",text).group())

"""
search
从头开始匹配，直到遍历到匹配的第一个
group(0)返回所有匹配的对象,group（1）匹配的第一个对象......
如re.match("(\w+) is ('w+),text).group(1) = Beautiful
"""
c = re.search("ugly",text)
print(c)

"""
sub
re.sub("要替换的字符串","替换成",搜索的文件，count替换几次）
默认替换所有
"""

"""
split

re.split(",",text)
"""

"""
findall
re.findall()返回所有匹配对象，列表形式
"""
re.findall("than (\w+)",text)#返回符合匹配条件的than后的对象
re.findall("href='(\w*.\w*)").findall()
#其中”.“表示点（href='image1.jpg')
"""
compile
预编译，增加运行速度
使用方法：
1.提前re.compile赋值给变量，再使用变量查找
2.re.compile("").findall(text)
"""


"""
常用：
^	匹配字符串的开头
$	匹配字符串的末尾。
.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
re*	匹配0个或多个的表达式。
re+	匹配1个或多个的表达式。
re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{ n}	精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
re{ n,}	匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
\w	匹配字母数字及下划线
\W	匹配非字母数字及下划线
\s	匹配任意空白字符，等价于 [\t\n\r\f].
\S	匹配任意非空字符
\d	匹配任意数字，等价于 [0-9].
\D	匹配任意非数字
\u4e00-\u9fa5 中文
"""
