person = {'name': 'zhangsan', 'age': 18, 'x': 'y'}
print(person['name'])

# 直接使用key可以修改对应的value
person['name'] = 'lisi'

# 如果key存在，是修改key对应的value
# 如果key在字典不存在，会往字典里添加一个新的key-value
person['gender'] = 'female'
print(person)

# pop把对应的键值对删除
# 执行结果是被删除的值
person.pop('name')
print(person)

# popitem删除一个元素，结果是被删除这个元素的键值对
result = person.popitem()
print(person)
print(result)

# clear方法用来清空一个字典
person.clear()
print(person)
