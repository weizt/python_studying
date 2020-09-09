# 函数的返回值就表示的函数的结果
def add(a, b):
    c = a + b
    return c


# 获取到add函数的结果，然后再求结果的4次方
result = add(1, 2)
print(result ** 4)

# 如果一个函数没有返回值，它的返回值就是None
x = print('hello')
print(x)  # None

# input就是一个有返回值的内置函数
age = input('请输入一个数据')
print(age)
