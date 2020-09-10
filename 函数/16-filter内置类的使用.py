# filter过滤，python2的时候是内置函数，python3修改成了一个内置类
# 对可迭代对象进行过滤，得到的是一个filter对象
ages = [12, 34, 23, 30, 17, 16, 19]
# filter可以给定2个参数，第一个参数是函数，第二个是可迭代对象
# filter结果是一个filter类型对象，filter对象也是一个可迭代对象
x = filter(lambda ele: ele > 18, ages)
for a in x:
    print(a)
