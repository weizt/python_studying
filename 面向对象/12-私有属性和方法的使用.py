# 类的私有变量
# 表示方式：__<var_name>，两个下划线开始的变量是私有变量
# 私有属性在类里可以访问，但是外面还是有一定办法可以访问的到
# 表示方式:__<function_name>,以两个下划线开始的是私有函数,可以在类内部调用
import datetime


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 定义了一个私有属性

    # 定义一个get函数获取私有属性，外部调用可以做很多事
    def get_money(self):
        print('{}调用了这个私有属性'.format(datetime.datetime.now()))
        return self.__money

    # 定义一个set函数用来修改私有属性
    def set_money(self, money):
        if type(money) != int:
            print('修改的数字不合法')
            return
        self.__money = money
        print('余额修改了')

    # 以两个下划线开始的,是私有函数,外部无法调用
    def __test(self):
        print('我是一个私有函数')


p = Person('zhangsan', 19)

# 获取私有变量的方式：
# 1.使用 对象名._类名__私有变量名   获取私有变量
# 2.使用 对象名._类名__私有函数名   获取私有函数
print(p._Person__money)
print(p._Person__test())

# 2.定义set和get方法猎取
print(p.get_money())

p.set_money(10000000)
print(p.get_money())
# 3.使用property获取
