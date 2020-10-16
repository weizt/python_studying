import re

# 1.数字和字母都表示它本身
re.search(r'x', 'dsajfxdafad')
re.search(r'6', '23897496823174')

# 2.多数字母前添加 \ 会有特殊含义
print(re.search(r'\d', 'alkjdflkds'))  # None \d 则不再表示字母d了

# 3.绝大多数标点符号都有特殊含义
print(re.search(r'+', '1+2'))  # 不能直接使用标点符号

# 4.如果想要使用标点符号,需要在前面加 \
print(re.search(r'\+', '1+2'))
