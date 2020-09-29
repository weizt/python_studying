import random

b = input('输入一个数字：')
a = 0
while a < int(b):
    list1 = []
    x = 1
    while x < 7:
        y = random.randint(1, 33)
        x += 1
        list1.append(y)
    print(sorted(list1), end='  ')

    z = random.randint(1, 16)
    print(z)
    a += 1
