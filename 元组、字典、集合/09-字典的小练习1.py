persons = [
    {'name': 'zhangsan', 'age': 18},
    {'name': 'lisi', 'age': 19},
    {'name': 'wangwu', 'age': 20},
    {'name': 'jack', 'age': 21},

]
# 让用户输入姓名，如果姓名已存在提示用户；如果姓名不存在，继续输入年龄，并存入列表
# in运算符，如果直接用在字典上，是用来判断key是否存在，而不是value
x = input('请输入你的姓名')
for person in persons:
    if person['name'] == x:
        print('你输入的姓名已存在')
    break
else:
    new_person = {'name': x}
    y = int(input('请输入你的年龄'))
    new_person['age'] = y
    persons.append(new_person)

print(persons)
