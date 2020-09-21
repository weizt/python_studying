person_list = []


# for i in range(len(persons)):
#     print(i)


# 添加名片信息功能
def add_person():
    name = input('请输入您的姓名： ')
    phone = (input('请输入您的手机号： '))
    address = input('请输入您来自哪座城市： ')
    job = input('请输入您的职业： ')
    person_dict = {'姓名': name, '电话': phone, '地址': address, '工作': job}
    person_list.append(person_dict)
    print('恭喜您，人员信息添加成功！')
    print(person_list)
    print()
    return person_dict


# 删除名片
def del_person():
    while True:
        del_name = input('请输入您想删除的人员姓名：')
        # flag = True  # 假设结果是真，那么下列的代码将不执行任何操作
        flag = False  # 定义变量flag = False,表示假设结果输入的名称与找果的名称不符
        for line in person_list:
            if del_name == line['姓名']:  # 判断条件证明flag=false是错误的
                flag = True  # flag变为True
                person_list.remove(line)
        if flag:  # if flag即如果flag为True，if =! True的意思，所以人员删除成功了
            # print('对不起，您要删除的对象不存在')
            print('恭喜您，已删除')
            print(person_list)
        else:
            # print('恭喜您，已删除')
            print('对不起，您要删除的对象不存在')
            break


# 修改名片
def change_person():
    while True:
        old_name = input('请输入您想修改人员的姓名(退出请输入exit)：')
        flag = True
        for line in person_list:
            if line['姓名'] == old_name:
                name = input('请输入新的姓名：')
                phone = input('请输入新的手机号：')
                address = (input('请输入您来自哪座城市：'))
                job = input('请输入您的工作：')
                line['姓名'] = name
                line['电话'] = phone
                line['地址'] = address
                line['工作'] = job
                flag = False
                break
        if flag:
            print('您想修改的人员信息不存在')
        else:
            print('人员信息修改已成功')
        print(person_list)
        if old_name == 'exit':
            break


# 查询名片
def find_person():
    find_name = input('请输入您想查找人员的姓名：')
    for person_dict in person_list:
        if person_dict['姓名'] == find_name:
            print('%s' % person_dict['姓名'])
            print('%s' % person_dict['电话'])
            print('%s' % person_dict['地址'])
            print('%s' % person_dict['工作'])
        else:
            print('抱歉，没有找到相关人员的信息')


# 显示所有名片
def show_person():
    if len(person_list) == 0:
        print('您所查看的系统中没有任何信息')

    for person in person_list:
        print(person)
    print('*' * 50)
    print()
    # print('%s/t%s/t%s/t%s/t'
    #       % (person_dict['name_str'],
    #          person_dict['phone_str'],
    #          person_dict['address_str'],
    #          person_dict['job_str'])
    #       )


while True:
    print('-' * 50)
    print('   名片管理系统V1.0    ')
    print('1.添加名片')
    print('2.删除名片')
    print('3.修改名片')
    print('4.查询名片')
    print('5.显示所有名片')
    print('6.退出系统')
    print('-' * 50)
    print()

    num = (input('请输入需要操作的数字：'))
    if num == '6':
        break
    elif num == '1':
        add_person()
    elif num == '2':
        del_person()
    elif num == '3':
        change_person()
    elif num == '4':
        find_person()
    elif num == '5':
        show_person()
    else:
        print('请输入正确的数字，谢谢！')
print()
