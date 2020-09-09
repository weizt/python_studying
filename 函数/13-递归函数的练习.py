# 使用递归求n!
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(4))


# 使用递归求斐波那契数据的第n个数字
# 1,1,2,3,5,8,13,21,34,55,89,144...
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(8))