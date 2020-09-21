# 定义一个类属性，刻录了创建了多个对象
class Person(object):
    __count = 0  # 定义一个类属性count，作为计数器  优化：使其为私有类属性

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        return object.__new__(cls)  # 申请内存，然后创建对象，对象类型为Person，
                                    # 这段代码就是不重写__new__方法，默认执行的代码

    def __init__(self, name, age):
     #  Person.__count += 1   这是通过计数__init__方法实现最简单的计数
        self.name = name
        self.age = age

    @classmethod
    def get_count(cls):
        return cls.__count


# 每次创建实例对象时都会调用 __init__ 和 __new__ 方法
# __new__方法，用来申请内存空间
# 如果不写重__new__，它会自动找object的__new__方法
# object的__new__方法，默认实现是申请段内存，创建一个对象
p1 = Person('张三', 2)
p2 = Person('张三', 32)
p3 = Person('张三', 12)

# 如果我们不重写__init__和__new__方法，也可以实现创建对象
# 下列代码就是直接创建实例对象的方法
p4 = object.__new__(Person)
p4.__init__('王五',19)
print(p4.name)

# 优化使计数器不能修改，外部无法调用修改

print(Person.get_count())
