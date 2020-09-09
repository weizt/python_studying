person = {'name': 'zhangsan', 'age': 18, 'height': '180cm'}
# 列表和元组是一个单一的数据，字典是键值对的形式
# 第一种遍历方式：
# for...in循环获取的是key
for x in person:
    print(x)
    print(x, '=', person[x])

# 第二种遍历方式
# 将key-value以元组的形式填入列表中
# 获取每一对键值对
print(person.items())
for item in person.items():
    print(item[0], '=', item[1])
# 以折包的方式真接获取键值对
for k, v in person.items():
    print(k, '=', v)

# 第三种遍历方式：
# 获取到所有的key，然后遍历key,根据key获取value
print(person.keys())  # dict_keys(['name', 'age', 'height'])
for k in person.keys():
    print(k, '=', person[k])

# 第四种遍历方式：
# 获取到所有的value
# 只能拿到value，不能拿到key
for v in person.values():
    print(v)


