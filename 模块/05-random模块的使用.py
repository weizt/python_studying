# random模块用来乱一个随机数
import random

# 用来生成[2,9]的随机整数
print(random.randint(2, 9))

# 用来生成[2,9)的随机整数
print(random.randrange(2, 9))

# 用来生成[0,1)的随机浮点数
print(random.random())

# 用来在可迭代对象里随机抽取一个数据
print(random.choice(['zhangsan', 'lisi', 'wangwu']))

# 有来在可迭代对象中随机抽取你定义的几个数据
print(random.sample(['zhangsan', 'lisi', 'wangwu', 'jack'], 2))
