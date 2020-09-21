# 单例设计模式概念:让多实例对象有且只有一个内存地址
# 设计思路：重写__new__方法，使创建实例对象时内存只申请一次 实例1 is 实例2 ==> True
# 实例：instance 对象：object 单例：singleton
class Singleton(object):
    __instance = None  # 创建一个类属性,最好是私有属性
    __first_str = True

    # 重写__new__方法
    @classmethod  # 定义类方法
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)  # object.__new__(cls) 这段是用来申请调用内存的代码
        return cls.__instance

    def __init__(self, a, b):
        if self.__first_str:
            self.a = a
            self.b = b
            self.__first_str = False  # 实例对象自己创建了self.__first_str = False，这个属性，无法修改类属性


# 1.调用__new__方法申请内存
# 2.如果不重写__new__方法，会调用object的__new__方法
# 3.object的__new__方法会申请内存
# 4.如果重写__new__方法，需要自己手动调用内存
s1 = Singleton('红色', '黄色')
s2 = Singleton('高山', '流水')

# 当设计实现单对象时，永远指向一块内存空间
# 无论创建多个实例对象，最后一个实例对象创建的会覆盖前一个实例对象的属性
# 永远保存最后一个实例对象的属性

# 如果想实现只显示第一次创建的实例属性，可以参考上述方法修改__init__方法，加判断
print(s1.a, s1.b)
print(s2.a, s2.b)

print(s1 is s2)
print(('0x%0X' % id(s1)))
print(('0x%0X' % id(s2)))
