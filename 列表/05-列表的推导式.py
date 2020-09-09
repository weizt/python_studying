# 列表推导式的作用就是使用简单的语句创建一个列表
nums = [i for i in range(10)]
print(nums)

x = [i for i in range(10) if i % 2]
# if语句后跟一个bool值，当i%2结果为0时，表示False时,则不打印，为True时打印
print(x)
# 打印结果为10以内的奇数

# points 是一个列表，这个列表中的元素是无组
points = [(x, y) for x in range(5, 9) for y in range(10, 20)]
print(points)

# 请写出一段python代码，代码实现分组一个list里的元素，比如[1,2,3...100]变成[1,2,3],[4,5,6]...
m = [i for i in range(1, 101)]
n = [m[j:j + 3] for j in range(0, 100, 3)]  # 使用切片实现列表里的元组为元素，range中加参数步长，实现间隔
print(n)
