# map内置类
ages = [12, 34, 23, 30, 17, 16, 19]
m = map(lambda ele: ele + 2, ages)
print(list(m))







# reduce以前是内置函数
# 内置函数和内置类都builtins.py文件
# reduce的一般是作用于求所有数据之和，也可作减法、乘法
from functools import reduce

scores = [100, 89, 76, 87]
x = reduce(lambda ele1, ele2: ele1 + ele2, scores)
print(x)



# 用reduce求所有学生年龄之和
students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': '180cm'},
    {'name': 'lisi', 'age': 28, 'score': 100, 'height': '170cm'},
    {'name': 'wangwu', 'age': 23, 'score': 90, 'height': '196cm'},
    {'name': 'jack', 'age': 21, 'score': 88, 'height': '176cm'},
    {'name': 'hoeny', 'age': 19, 'score': 65, 'height': '163cm'}
]


def bar(x, y):
    return x + y['age']


# reduce最后要加一个参数0，表示初始化X的值，否则X和Y都取students中的字典对象
print(reduce(bar, students, 0))
