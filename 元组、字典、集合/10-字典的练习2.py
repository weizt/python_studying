dict1 = {'a': 100, 'b': 200, 'c': 300}
# 使用方法使dict1的key-value变换位置
dict2 = {}
for k, v in dict1.items():
    dict2[v] = k
print(dict2)

# 字典推导式
dict1 = {v: k for k, v in dict1.items()}
print(dict1)
