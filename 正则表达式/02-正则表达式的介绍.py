# 用来处理字符串，对字符串进行检索和替换
# 功能：1.查找 2.替换

# re是正则表达式的模块
import re

x = 'hello\\world'
print(x)  # hello\world

# 在正则表达式里，如果想匹配一个\，需要使用\\\\

# match:匹配 ; search:检索 执行结果都是一个Match类型的对象
# 第一个参数表示正则匹配规则；第二个参数表示需要匹配的字符串

# m = re.search('\\\\', x)
m = re.search(r'\\', x)  # 功能同上
print(m)  # <re.Match object; span=(5, 6), match='\\'>
