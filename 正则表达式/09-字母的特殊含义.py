import re

# 字母表示它本身，很多字母前面加 \ 有特殊含义

# \n:表示换行
# \t:表示制表符
# \s:表示空白字符
# \S:表示非空白字符

# \d:表示数字，等价于[0-9]
m1 = re.search(r'x\dp', 'x8p')  # 只能匹配一个数字
m1_1 = re.search(r'x\d+p', 'x88989p')  # 匹配出现一次或多次的数字用 +
print(m1)  # ==> <re.Match object; span=(0, 3), match='x8p'>

# ^除了表示以指定的内容开始，还可以在[]里表示取反
# \D:表示非数字，等价于[^0-9]
m2 = re.search(r'\D+', 'adfdsaf97987897')
m2_1 = re.search(r'[^0-9]+', 'adfdsaf97987897')  # 等价于m2
print(m2)  # ==> <re.Match object; span=(0, 7), match='adfdsaf'>

# \w:表示数字、字母、中文以及 _ 所有其他非标点符号字符
m3 = re.findall(r'\w+', 'h+E-11.0_X')  # 使用findall()方法拿到所有组合
m3_1 = re.findall(r'\w+', '大-家+好！')
print(m3)  # ==> ['h', 'E', '11', '0_X']
print(m3_1)  # ==>['大', '家', '好']

# \W:表示取标点符号，与\w取反
m4 = re.findall(r'\W+', 'h+E-11.0_X')
print(m4)  # ==>['+', '-', '.']
