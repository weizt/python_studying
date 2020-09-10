import time


def cal_time(fn):
    print('我是外部函数，我被调用了')
    print('fn={}'.format(fn))

    def inner():
        start_time = time.time()
        fn()
        end_time = time.time()
        print('代码耗时{}'.format(end_time - start_time))

    return inner  # 这时要注意不能加括号，要返回inner这个函数名，而不调用inner这个函数


# 调用装饰器函数
# 执行步骤1：调用cal_time:
# 执行步骤2：把被装饰的函数传给fn
# 执行步骤3：此时的demo函数已经变成了inner函数
@cal_time
def bar():
    print('122')
    time.sleep(3)
    print('90')


# def demo():
#     y = 1
#     for i in range(1, 10000000):
#         y += i
#     print(y)


print('bar={}'.format(bar))
bar()

import time


def cal_time(fn):
    print('我是外部函数，我被调用了')
    print('fn={}'.format(fn))

    def inner():
        start_time = time.time()
        fn()
        end_time = time.time()
        print('代码耗时{}'.format(end_time - start_time))

    return inner  # 这时要注意不能加括号，要返回inner这个函数名，而不调用inner这个函数


# 调用装饰器函数
# 执行步骤1：调用cal_time:
# 执行步骤2：把被装饰的函数传给fn
# 执行步骤3：此时的demo函数已经变成了inner函数
@cal_time
def bar():
    print('122')
    time.sleep(3)
    print('90')


@cal_time  # 想对多个函数进行装饰，使用多个@cal_time
def demo():
    y = 1
    for i in range(1, 10000000):
        y += i
    print(y)


print('bar={}'.format(bar))
bar()

print(demo)  # 被装饰后的函数deom()则成为装饰器函数的内部函数了inner()
demo()

