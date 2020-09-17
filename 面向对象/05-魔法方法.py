# 魔法方法:也叫魔术方法,是类里的特殊的一些方法
'''
特点:
1.不需要手动调用,会在合适的时机自动调用
2.这些方法,都是使用__开始,使用__结束
3.方法名都是系统规定好的,在合适的时机自己调用
'''


class Person(object):
    def __init__(self, name, age):
        # 在创建对象时,会自动调用这个方法
        print('__init__被调用了')
        self.name = name
        self.age = age

    def __del__(self):
        # 当对象被销毁时,自动调用此方法
        # 程序执行完毕后,也会自动调用此方法
        print('__del__方法被调用了')

    def __repr__(self):
        return '456'

    # 当需要打印一个对象时,可以选择调用__str__方法
    def __str__(self):
        return '姓名:{},年龄{}'.format(self.name, self.age)

    # 调用对象,相当于调用对象的__call__方法
    def __call__(self, *args, **kwargs):
        print('__call__方法被调用了')
        # *args 为一个元组,保存任意参数
        # **kwargs 为一个字典,保存关键字参数
        print('args={},kwargs={}'.format(args, kwargs))
        fn = kwargs['fn']
        return fn(args[0], args[1])


p = Person('zhangsan', 18)
# 如果不作修改,直接打印这个实例对象,那么打印的将是文件__name__的类型和内存地址
# 当打印一个对象的时候,会调用这个对象的__str__或者__repr__方法的返回值
print(p)  # ==> <__main__.Person object at 0x0000000001DB0D48>

# 魔术方法一般不手动调用,如果手动调用可用下面这些方法
# 简单理解就是手动调用这个实例对象所属的类里的魔术方法的返回值
print(p.__repr__())
print(repr(p))  # 调用内置函数repr,会触发__repr__方法

# 把对象当函数来调用,  对象名()   表示调用这个对象的__call__方法,直接调用p()会报错
result = p(1, 3, fn=lambda x, y: x + y)  # 实例对象调用用__call__方法的拓展写法
print(result)

# del p  # 手动销毁对象,调用__del__方法
