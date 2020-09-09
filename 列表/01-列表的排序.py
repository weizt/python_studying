# 调用列表的 sort 方法直接对列表进行排序
nums = [5, 2, 6, 3, 8, 0, 9, 1]
nums.sort(reverse=True)  # reverse=True 表示对列表进行反向排序
print(nums)

# sorted() 是内置函数，不会改变原来的列表排序，生成一个新的排序后的列表
nums1 = [5, 2, 6, 3, 8, 0, 9, 1]
x = sorted(nums1)  # 内置函数sorted不会改变原有的列表排序
print(x)
print(nums1)

# 调用列表的reverse方法可对列表进行反转
names = ['zhangsan', 'lisi', 'wangwu']
names.reverse()
print(names)
print(names[::-1])  # 字符串的切片方法也可对列表进行反转
