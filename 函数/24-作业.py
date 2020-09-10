persons = []


def add_person():
    person = {'name': None, 'age': None, 'address': None, 'height': None}
    person['name'] = input('请输入您的姓名： ')
    person['age'] = int(input('请输入您的年龄： '))
    person['address'] = input('请输入您来自哪座城市： ')
    person['height'] = input('请输入您的身高： ')
    persons.append(person)
    print(person)
    return person
add_person()

x = 0
while x < 100000:
    print('   名片管理系统V1.0    ')
    print('1.添加名片')
    print('2.删除名片')
    print('3.修改名片')
    print('4.查询名片')
    print('5.显示所有名片')
    print('6.退出系统')
    print('--------------------------------------------')

    num = int(input('请输入需要操作的数字：'))
    x += 1
    if num == 6:
        break
    elif num == 1:
        add_person()
    elif num != 1 or num != 2 or num != 3 or num != 4 or num != 5 or num != 6:
        print('请输入正确的数字，谢谢！')
