# 列表可以使用extend方法将两个列表合并成一个列表
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 0]
nums1.extend(nums2)
print(nums1)
# 方法2：使用+连接两个列表
print(nums1 + nums2)

# 元组也可以使用+来连接两个元组，生成一个新元组
# 元组是不可变数据类型，无法修改
word1 = ('hello', 'good')
word2 = ('yes', 'ok')
print(word1 + word2)

# 字典中可以使用update方法将两个字典合并成一个字典
# 字典之间不支持+运算，只能使用update方法
person = {'name': 'zhangsan', 'age': 18}
person2 = {'addr': 'anhui', 'height': 180}
person.update(person2)
print(person)
