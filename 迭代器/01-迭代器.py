# 可迭代对象：list/tuple/dict/set/str/range/filter/map
# for..in... 可迭代对象

# isinstance(变量名,类名): isinstance用来判断一个实例对象是不是指定的类型
from collections.abc import Iterable

lists = list(('zhangsan', 'list'))  # 就是系统内置类创建的实例对象

print(isinstance(lists, Iterable))


# class foo(object):
#     def __next__(self):
#         return 1

class Demo(object):
    def __init__(self, x):
        self.x = x
        self.count = 0

    # 只要将定义的类重写__iter__方法，这个类就是一个可迭代对象
    def __iter__(self):
        return self

    # 可以直接自己返回自己，然后重写__next__方法，return什么，循环什么
    def __next__(self):
        self.count += 1
        if self.count <= self.x:
            return 'for..in循环的本质'
        else:
            raise StopIteration  # 使用rasie关键字抛出异常，用于停止循环


d = Demo(10)
print(isinstance(d, Iterable))

# for..in... 循环的本质就是调用可迭代对象__iter__方法，获取到这个方法的返回值
# 这个返回值是一个迭代器对象，然后再用这个对象的__next__方法
for i in d:
    print(i)
