# 去重排序
first = ['李白', '白居易', '李清照', '杜甫', '王昌龄', '王维', '孟浩然', '王安石']
second = list(set(first))
print(second)
print(second.sort(reverse=True))

# 内置类互相转换 list,tuple,set
nums = [9, 8, 6, 4, 2, 1]
x = tuple(nums)
print(x)

y = set(nums)
print(y)


