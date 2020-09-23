# 定义可变参数,*args表是可变位置参数
# 多出来的可变参数，会以元组的形式保存到args中

# a,b表示必须最少有两个参数
def add(a, b, *args):
    c = a + b
    for arg in args:
        c += arg
    return c


# 缺省参数必须写在可变参数的后面
def add_1(a, b, *args, mul=1):
    c = a + b
    for arg in args:
        c += arg
    return c * mul


# args可变参数表示到0-无数个参数
def add_2(*args):
    c = 0
    for arg in args:
        c += arg
    return c


# **kwargs表示可变的关键字参数
# 多的关键字参数会以字典的形式保存
def add_3(a, b, *args, mul=1, **kwargs):
    print('kwargs={}'.format(kwargs))
    c = a + b
    for arg in args:
        c += arg
    return c * mul


print(add_3(1, 2, 3, mul=5, t=1, y=2))
