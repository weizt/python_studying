class Demo(object):
    def __enter__(self):
        print('__enter__方法被调用了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__方法被调用了')


def creat_obj():
    x = Demo()
    return x


# y = creat_obj()
# d = y.__enter__()  这段代码等同于下面的with关键后面的代码块

with creat_obj() as d:  # as后面加变量名
    # 变量d 不是creat_obj的返回结果
    # 它是创建对象 y 调用__enter__方法之后的返回结果
    print(d)
