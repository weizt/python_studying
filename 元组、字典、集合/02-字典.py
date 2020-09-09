# 列表可以存储任意数据类型，但一般情况下，我们只存储单一数据类型
# 列表只能存储值，但是无法对值进行描述
# dict
# 字典不仅可以保存值，还可以对值进行描述
# 使用大括号来表示一个字典，不仅有值value，还有值的描述key
# 字典里的数据都是以键值对key-value的形式保留的
# key和value之间用冒号：来连接
# 多个键值对之间用逗号，来分隔
# 字典里的key不允许重复，如果key重复了，后一个key对应的值会覆盖前一个
# 字典里的value可以是任意数据类型，但是key只能使用不可变数据类型

person = {
    'name': 'weizhetao',
    'age': 18,
    'math': 98,
    'height': 180,
    'weight': 60,
    'isPass': True,
    (100, 200): 'ok',
    5: 6
}
a = []
for i in person:
    a.append(i)
    print(a)
print(person, sep='\n')
print(1, 2, 3, 4, 5, sep='\n')
