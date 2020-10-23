import re

# \s 表示任意的空白字符
print(re.search(r'\s', 'hello world'))  # 空格 <re.Match object; span=(5, 6), match=' '>

print(re.search(r'\n', 'hello\nworld'))  # 换行 <re.Match object; span=(5, 6), match='\n'>
print(re.search(r'\t', 'hello\tworld'))  # 制表符 <re.Match object; span=(5, 6), match='\t'>

# \S 表示非空白字符
print(re.search(r'\S', '\n\t   x'))  # <re.Match object; span=(5, 6), match='x'>

# 标点符号的使用：表示特殊含义的标点符号，如果要使用它们，必须加前面要\反斜杠表示转义

# ():表示一个分组
m = re.search(r'h(\d+)x', 'sh829xkflsa')  # 加括号表示分组
print(m.group(1))  # ==>829
m1 = re.search(r'\(.*\)', '(1+1)*5+5')  # 加\将括号转义，以左括号开号，以右括号结束的内容
print(m1.group())  # ==>(1+1)

# . : 表示匹配除换行以外的任意字符
m2 = re.search(r'\.', 'dsfadsa..asfsda.dsafds')  # 加\表示匹配 . ，不加表示除任意字符，取到第一个则结束
print(m2.group())

# []:用来表示可选项，区间，范围
m3 = re.search(r'f[0-5]m', 'f5masd')  # 以f开始，以m结束，中间的数字在0-5之间，包括0和5，只匹配一个数字
m3_1 = re.search(r'f[0-9]+m', 'f5897masd')  # 以f开始，以m结束，中间的数字在0-5之间，包括0和5，加个 + 表示匹配一次或多次
m3_2 = re.search(r'f[a-z]m', 'fxmasd')  # 以f开始，以m结束，中间的字母在a-z之间，包括a和z，只匹配一个字符
m3_3 = re.search(r'f[0-5a-zx]m', 'fxmasd')  # 以f开始，以m结束，中间的字母在a-z之间，包括a和z；或者0-5，包含0和5；或者包括x
print(m3.group())  # ==> f5m
print(m3_1.group())  # ==> f5897m
print(m3_2.group())  # ==> fxm
print(m3_3.group())  # ==> fxm

# | :用来表示或者的关系。与[]有一定相似性，但区别在于|是匹配可选值，可以是多个字符；[]是匹配区间，而且只能是单个字符
m4 = re.search(r'a(b|cdf|d)z', 'acdfz')  # 匹配a开始始结束，中有b或者c或者d的字符
print(m4.group())

# {} :用来限定前面元素出现的次数
m5 = re.search(r'go{2}d', 'good morning')  # {n}:表示前面的元素出现n次
print(m5.group())
m5_1 = re.search(r'go{2,}d', 'gooooood morning')  # {n,}:表示前面的元素出现n次以上
print(m5_1.group())
m5_2 = re.search(r'go{,2}d', 'god morning')  # {,n}:表示前面的元素出现n次以下
print(m5_2.group())
m5_3 = re.search(r'go{3,5}d', 'gooood morning')  # {m,n}:表示前面的元素出现m到n次
print(m5_3.group())

# * :表示前面的元素出现任意次数(0次及以上，等价于{0,})
m6 = re.search(r'go*d', 'gooood')
print(m6.group())

# + :表示前面的元素出现任意次数(1次及以上，等价于{1,})
m7 = re.search(r'go+d', 'goooood')
print(m7.group())

# ? : 1.规定前面的元素最多只能出现一次，等价于{,1}
#     2.将贪婪模式转化成非贪婪模式
m8 = re.search(r'go?d', 'god')
print(m8.group())

# ^ :以指定的内容开头，还可以表示在[]中取反  $ :指定内容结尾
m9 = re.search(r'^a.*i$', 'adlfsi  kfjlsdi')  # 必须是以a开头，以i结尾，并且可以匹配空格
print(m9)  # <re.Match object; span=(0, 13), match='adlfsi   kfjlsdi'>

