# 定义好的函数，还可以以赋值的形式起一个别名，功能完全相同
def adds(a, b):
    return a + b


fn = adds


# 在python中除了使用def关键字定义一个函数以外，还可以使用lambda表达式定义一个函数
# 匿名函数，用来表达一个简单的函数，基本只调用一次
# lambda c, d: c + d


# 调用匿名函数的两种方式：
# 1.给它定义一个名字（不常用）
# 2.把这个函数当作参数传给另一个函数使用（常用）

# 自定义一个匿名函数的使用场景
def calc(a, b, fn):
    c = fn(a, b)
    return c


# 当函数当作另一个函数的参数调用,回调函数
def add(x, y):
    return x + y


x1 = calc(1, 2, add)
print(x1)

# 使用lambda关键字创建匿名函数,作为参数
# 表示函数中调用匿名函数作用参数使用
x3 = calc(5, 7, lambda x, y: x + y)
print(x3)
x4 = calc(19, 7, lambda x, y: x * y)
print(x4)
