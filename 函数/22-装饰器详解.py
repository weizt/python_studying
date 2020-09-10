import time


def cal_time(fn):
    print('我是外部函数，我被调用了')
    print('fn={}'.format(fn))

    def inner(p):  # 由于此时的inner()= demo()，所以也必须加参数，参数是形参
        # def inner(p,*args,**kwargs):  # 这里可以加多个参数了，但不影响原本的demo函数
        start_time = time.time()
        s = fn(p)  # fn就是dinner函数，所以也要加参数，且参数为实参，区别与innen(p)
        end_time = time.time()
        print('代码耗时{}'.format(end_time - start_time))
        return s

    return inner  # 这时要注意不能加括号，要返回inner这个函数名，而不调用inner这个函数


@cal_time
def demo(n):  # 若被装饰函数加了参数
    y = 1
    for i in range(1, n):
        y += i
    return y


print('demo={}'.format(demo))  # 被装饰后的函数deom()则成为装饰器函数的内部函数了inner()
demo(1000)  # demo函数不变，但被装饰的函数可以增加多个参数了

# 关键：只要是加了装饰器的函数，就变成了内部函数，内部函数返回什么结果就是什么结果


import time


def cal_time(fn):
    print('我是外部函数，我被调用了')
    print('fn={}'.format(fn))

    def inner(p, *args, **kwargs):  # 由于此时的inner()= demo()，所以也必须加参数，参数是形参
        # def inner(p,*args,**kwargs):  # 这里可以加多个参数了，但不影响原本的demo函数
        start_time = time.time()
        s = fn(p)  # fn就是dinner函数，所以也要加参数，且参数为实参，区别与innen(p)
        end_time = time.time()
        print('代码耗时{}'.format(end_time - start_time))
        return s

    return inner  # 这时要注意不能加括号，要返回inner这个函数名，而不调用inner这个函数


@cal_time
def demo(n):  # 若被装饰函数加了参数
    y = 1
    for i in range(1, n):
        y += i
    return y


print('demo={}'.format(demo))  # 被装饰后的函数deom()则成为装饰器函数的内部函数了inner()
demo(1000, 'good', s='hello')  # demo函数不变，但被装饰的函数可以增加多个参数了

# 关键：只要是加了装饰器的函数，就变成了内部函数，内部函数返回什么结果就是什么结果


