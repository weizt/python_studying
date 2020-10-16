# 调用re.方法名。拿到的内容都是re.Match类型的对象

import re

# .表示任意字符 *表示任意次数
m = re.search(r'm.*a', 'dskjafdmkldsjal')

# 查看re.Match类拥有的属性
print(dir(m))
list = ['__class__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
        '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
        '__ne__',
        '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
        '__subclasshook__',
        'end', 'endpos', 'expand', 'group', 'groupdict', 'groups', 'lastgroup', 'lastindex', 'pos', 're', 'regs',
        'span',
        'start', 'string']

# span()方法:匹配的结果字符串开始和结束的下标
print(m.span())  # (7, 14)

# group()获取匹配的字符串结果，group可以传参，表示第n个分组
# 1.在正则表达式里使用()表示一个分组
# 2.如果没有分组，默认只有一个分组
# 3.分组的下标从0开始
# 共有5组，最大的为第0组
m1 = re.search(r'(0.*)(3.*)(5.*)(7.*9)', '0ksdj3lakf5jlkds7ajlk9fj')
print(m1.group())  # 0ksdj3lakf5jlkds7ajlk9
print(m1.group(0))  # 0ksdj3lakf5jlkds7ajlk9
print(m1.group(1))  # 0ksdj
print(m1.group(2))  # 3lakf
print(m1.group(3))  # 5jlkds
print(m1.group(4))  # 7ajlk9
# print(m1.group(7))  没有则会报错
print(m1.groups())  # ('0ksdj', '3lakf', '5jlkds', '7ajlk9') 将所有匹配的组存入到一个元组

# (?P<name>表达式) 给分组起一个名字，存入字典，?为英文格式，P要大写
m2 = re.search(r'(0.*)(?P<xxx>3.*)(5.*)(7.*9)', '0ksdj3lakf5jlkds7ajlk9fj')
print(m2.groupdict())  # {'xxx': '3lakf'}
print(m2.groupdict('xxx'))