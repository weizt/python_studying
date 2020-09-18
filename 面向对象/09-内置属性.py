class Person(object):
    __slots__ = ('name','age')
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭')


# 行为也可以理解为一种属性，其类型为函数 eat():<function>，name:'张三'，age:18
p1 = Person('张三', 18)

# dir()方法就对象所有的属性打印出来
print(dir(p1))

print(p1.__class__)  # <class '__main__.Person'>
# print(p1.__dict__)  # 将对象转换成字典 {'name': '张三', 'age': 18}
print(p1.__dir__())
print(p1.__doc__)  # 打印多行注释的内容 调用方法 class_name.__doc__ 或者 object_name.__doc__
print(p1.__module__) #__main__
print(p1.__slots__) # 规定这个类能出现的属性