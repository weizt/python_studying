# 集合(set)是一个无序的不重复的元素序列，可以使用大括号或者set()函数来创建集合
# 注意：创建一个空集合必须用set()来实现，不能用{}，因为{}是用来创建一个空字典
x = {'hello', 1, 'ok'}  # 这就是一个集合

# 如果有重复的数据 ，自动去重
names = {'zhangsan', 'lisi', 'jack', 'tony', 'jack', 'lisi'}
print(names)

# 空集合用set()表示
# set的增删改
# 添加一个数据
names.add('wangwu')
print(names)

# 清空一个集合
# names.clear()
print(names)

# 随机删除一个元素
names.pop()
print(names)

# 删除一个指定的元素
names.remove('jack')
print(names)

# union 将多个集合合并并生成一个新的集合
# A.update（B）是将B拼接到A里
# B为可迭代对象，列表，元组都可以放在A中
names.update({'赵四', '刘能'})
print(names)
