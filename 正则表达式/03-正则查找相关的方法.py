# 查找相关的方法
# match 和 search:
# 共同点:1.只对字符串查询一次;2.返回值类型都是re.Match类型的对象
# 不同点:match 是从头开始匹配，一旦匹配失败，就返回None;
#       search 是在整个字符串中匹配，如果有多个匹配对象，只匹配第一个
# finditer:查找到所有匹配到的数据，放到一个可迭代对象中
# findall:查找到所有匹配到的数据，放到一个列表中
# fullmatch:完整匹配，需要字符串完全满足正则规则


import re
from collections.abc import Iterable

m1 = re.match(r'good', 'hellogood')
print(m1)  # None
m2 = re.search(r'good', 'hellogood')
print(m2)  # <re.Match object; span=(5, 9), match='good'>

# finditer: 返回值是一个可迭代对象
# 可迭代对象里的数据是匹配到的结果，都是一个re.Match类型的对象
m3 = re.finditer(r'x', 'klxsdajxflkxdsxdjax')
print(isinstance(m3, Iterable))  # True
print(m3)  # <callable_iterator object at 0x0000000002131408>

# mm_list= []
# mm = list(filter(lambda s: s == 'x', m3))
# print(mm_list.append(mm))
for m in m3:
    print(m)

# findall：查找到x后面加数字的结果
m4 = re.findall(r'x\d+', 'klx67sdajx78flkxdsxdjax')
print(m4)  # ['x67', 'x78']

# fullmatch:完整匹配
m5 = re.fullmatch(r'hello world', 'hello world')
print(m5)  # <re.Match object; span=(0, 11), match='hello world'>
