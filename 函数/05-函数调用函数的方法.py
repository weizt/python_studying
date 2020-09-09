# 函数只要不调用，就不执行
def test1():
    print('t1开始')
    print('t1结束')


def test2():
    print('t2开始')
    test1()
    print('t2结束')


test2()


# 定义函数求n~m之间所有整数之和
def count(n, m):
    nums = 0
    for i in range(n, m):
        nums += i
    return nums


print(count(0, 101))


# 定义一个函数，求n的阶乘
def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


print(factorial(5))


# 计算m的阶乘之和
def fac_sum(m):
    x = 0
    for i in range(1, m + 1):
        x += factorial(i)  # 调用factorial函数
    return x


print(fac_sum(5))
