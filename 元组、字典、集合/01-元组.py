# 元组和列表很像，都是用来保存多个数据
# 使用一对（）来表示一个元组
# 元组和列表的区别在于，列表是可变，而元组是不可变的
words = ['hi', 'hello', 'good', 'yes']
nums = (9, 4, 3, 5, 2, 6, 7, 9)

# 元组和列表一样，也是一个有序的存储数据的容器
# 可以通过下标的方式来获取元素
print(nums[3])

# nums[3]=40 元组是不可变数据类型，不可修改里面的元素
# 元组的方法
print(nums.index(7))
print(nums.count(9))

# 特殊情：如何表示只有一个元素的元组
ages = (18)  # 这种书写方式，a是一个整数，不能表示元组
ages1 = (18,)  # 在唯一的一个元素后面加一个逗号，表示元组
words1 = ('hello')
print(tuple(words1))  # ('h', 'e', 'l', 'l', 'o') 无组类型中的数据必须是可迭代对象

# 如何将元组和列表相互转换
print(tuple(words))  # 使用tuple内置类
print(list(nums))  # 使用list内置类

# 元组中使用join方法
heights = ('180', '190', '170')
# join方法所带的参数必须是字符串和可迭代对象
# join方法就是用各种字符将可迭代对象连接起来
print('*'.join(heights))

# 元组也可以遍历
for i in nums:
    print(i,end='-')

# 用while方法实现遍历
j = 0
while j < len(nums):
    print(nums[j])
    j += 1
