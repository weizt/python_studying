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

# 手动的for...in...循环。本质就是调用对象的.__iter__().__next__()方法
# print(d.__iter__().__next__())

i = iter(d)  # 内置函数 iter()方法可以获取到一个可迭代对象的迭代器
print(next(i)) # 跟上面的代码功能一致
print(next(i))
print(next(i))
