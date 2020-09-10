import time  # time模块可以获取当前的时间

# 在代码运行之前，获取一下时间
# time模块里的time方法，可以获取当前的时间戳
# 时间戳是从1970-01-01 00：00：00 UTC到至今
stat_time = time.time()
x = 0
for i in range(1, 100000000):
    x += i
print(x)

# 代码完成后再获取一下时间
end_time = time.time()
print(end_time - stat_time)


# 优化计算代码运算时长的方案
# 方案思路：
# 1.把计算时长封装成一个函数
# 2.把需要计算时长的代码块封装成一个函数
# 3.在把第二个函数当作第一个函数的参数
# 4.传参调用
def time_count(fn):
    stat_time1 = time.time()
    fn()
    end_time2 = time.time()
    print('代码计算的时长为：{}'.format(end_time2 - stat_time1))


def demo():
    y = 1
    for u in range(1, 1000000):
        y += u
    print(y)


def foo():
    print('123')
    time.sleep(3)
    print('234')


time_count(demo)
time_count(foo)
