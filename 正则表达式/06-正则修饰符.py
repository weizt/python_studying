import re

# 正则修饰符是对正则表达式进行修饰
# 正常情况下 . 表达非换行以外的任意字符
# re.S  让 . 匹配换行
x = re.search(r'm.*a', 'dafdasmf\nsafsdafklja', re.S)
print(x)  # <re.Match object; span=(6, 20), match='mf\nsafsdafklja'>

# re.I  忽略大小写
y = re.search(r'x', 'DXZYX', re.I)
print(y)  # <re.Match object; span=(1, 2), match='X'>

# \w:表示的是字母数字和_   +:出现一次以上   $:以指定的内容结尾
# re.M  让 $ 匹配换行
z = re.findall(r'\w+$', 'i am boy\n you are girl\n he is man', re.M)
print(z)  # ['boy', 'girl', 'man']
