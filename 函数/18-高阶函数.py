# 1. 一个函数作为另一个函数的返回值
# 2.一个函数作为另一个函数的参数（lambda匿名函数）
# 3.在函数内部再定义一个函数

# 函数作为另一个函数的返回值
def foo():
    print('我是foo,我被调用了')
    return 'wzt'


def bar():
    print('我是bar，我被调用了')
    # return foo()  # 函数foo()作为函数bar()返回值，在调用bar()时，会再次调用foo()
    return foo  # 若不加括号则返回值不是调用函数foo(),而是返回foo这个函数名，打印的是函数这个对象


bar()  # 此时函数bar没有给定变量进行赋值，所以不打印返回值wzt
x = bar()  # 给定bar()返回值赋值给x,打印x的结果就有wzt;若不加括号的情况下x=foo(),x是foo()别名
print('x的值是{}'.format(x))

bar()()  # 先调用bar()，再调用foo()

print('-----------------------------------')


# 在函数内部再定义一个函数
def outer():
    def inner():
        print('我是inner函数')

    print('我是outer函数')
    return inner


# 先调用外部函数，外部函数再把内部函数作为返回，调用时加两个括号（同上）
outer()()


# 在函数内部再定义一个函数
def outer(x):
    m = 100  # 局部变量

    def inner():  # inner是定义outer函数内部的一函数
        print('我是inner函数')

    if x > 18:
        inner()
    return 'hello'


# print(m)
# inner()
outer(12)
outer(32)