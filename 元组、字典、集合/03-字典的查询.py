# 字典查找数据，数据保存时，是无序的，，不能通过下标获取
# 通过键来查找,使用key获取到对应的value
# key一般为字符串，要加引号‘’
# 如果要查找的key不存在，会直接报错
person = {'name': 'zhangsan', 'age': 18, 'x': 'y'}
print(person['name'])
x = 'age'
print(person[x])

# 需求：获取一个不存在的key时，不报错，如果这个key不存在，使用默认值
# 使用字典的get方法
print(person.get('height'))  # None

# 如果根据key获取不到value，使用给定的默认值
# 如果找到了对应的value，就不会使用默认值
# 使用get方法，不会往字典中增加数据
print(person.get('gender', 'female'))
