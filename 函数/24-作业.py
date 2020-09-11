persons = []


# 添加名片信息功能
def add_person():
    person = {'name': None, 'phone': None, 'address': None, 'job': None}
    person['name'] = input('请输入您的姓名： ')
    person['phone'] = (input('请输入您的手机号： '))
    person['address'] = input('请输入您来自哪座城市： ')
    person['job'] = input('请输入您的职业： ')
    persons.append(person)
    print(person)
    print()
    return person


# add_person()

# 删除名片
def del_person():
    serial_num = int(input('请输入您想删除的名片序号：'))
    for i in range(0,len(persons)-1):
        if i == serial_num:
            persons.pop(serial_num)
            print('您删除了序号为{}的人员'.format(serial_num))
        else:
            print('您删除的人号不存在，请重新输入')


# 修改名片
# 查询名片
# 显示所有名片




while True:
    print('   名片管理系统V1.0    ')
    print('1.添加名片')
    print('2.删除名片')
    print('3.修改名片')
    print('4.查询名片')
    print('5.显示所有名片')
    print('6.退出系统')
    print('--------------------------------------------')

    num = int(input('请输入需要操作的数字：'))
    if num == 6:
        break
    elif num == 1:
        add_person()
    elif num == 2:
        del_person()
    elif num not in (1, 2, 3, 4, 5, 6):
        print('请输入正确的数字，谢谢！')
print()

# 测试
