# compile 编译
# 在re模块中，可以使用re.方法名 调用函数，也可以使用re.compile得到一个对象，再调用函数

import re

# 直接调用函数
m = re.search(r'm.*a', 'dskjafdmkldsjal')
print(m)  # <re.Match object; span=(7, 14), match='mkldsja'>

# 先使用compile创建对象，再用对象调用函数，效果等同于上
x = re.compile(r'm.*a')
m1 = x.search('dskjafdmkldsjal')
m2 = x.search('dlskajfmklsdakasfdsafdsamasdfsdalfj')
print(m1)  # <re.Match object; span=(7, 14), match='mkldsja'>

# 生成一个正则规则，适用于不同的字符串对象，compile使用率更高

