# 需求：使用用迭代器生成斐波那契数据
class Fibonacci(object):
    def __init__(self, x):
        self.x = x
        self.num1 = self.num2 = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.x:
            y = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return y
        else:
            raise StopIteration


# 多占时间，少占空间
num = Fibonacci(20)
for i in num:
    print(i)

# 有列表，为什么还要迭代器？ 省内存
