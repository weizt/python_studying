import file_manager
import model

base_dir = './files/'
name = ''


# students_list = [] 添加学生生时，要先读取这个json文件，所以不能这样写，否则每次运行都会覆盖这个数据，之前的数据就没有了


def add_student():
    # 要先读取老师的json文件，没有时，创建一个新字典，有则拿出原有的数据再重写一遍这个json文件，保证数据的持久性
    stu_tea_json = file_manager.read_json(name + '.json', {})
    if not stu_tea_json:
        students_list = []
        num = 0

    else:
        students_list = stu_tea_json['all_students']
        num = int(stu_tea_json['num'])

    while True:
        stu_name = input('请输入学生的姓名：')
        stu_age = input('请输入学生的年龄：')
        stu_sex = input('请输入学生的性别：')
        stu_tel = input('请输入学生的电话：')

        num += 1
        # 字符串的zfill()方法，在字符串前补0
        s_id = 'stu' + str(num).zfill(4)

        # 导入model模块，创建一个学生类的实例对象
        student = model.Student(s_id, stu_name, stu_age, stu_sex, stu_tel)

        students_list.append(student.__dict__)
        data = {'all_students': students_list, 'num': len(students_list)}
        # print(data)
        # 将data保存到一个json文件，调用file_manager模块中的write_json方法
        file_manager.write_json(name + '.json', data)

        choice = input('添加成功！\n1.继续\n2.返回\n请选择(1~2):')
        if choice == '1':
            continue
        elif choice == '2':
            break
        else:
            print('输入错误，请重新选择！')
            break


def show_student():
    operator = input('1.查看所有学生\n2.根据姓名查找\n3.根据学号查找\n其他：返回\n请选择：')
    stu_json_file = file_manager.read_json(name + '.json', {})
    students = stu_json_file.get('all_students', [])
    if not students:
        print('该老师还没有添加学生，请先添加！')
        return

    if operator == '1':
        for stu in students:
            print('学号:{s_id},姓名:{name},性别:{sex},年龄:{age},☎:{tel}'.format(**stu))
    elif operator == '2':
        stu_name = input('请输入学生姓名:')
        stu_search_name = []
        for stu in students:
            if stu['name'] == stu_name:
                stu_search_name.append(stu)
        if not stu_search_name:
            print('没有找到此姓名的学生')

        # 简写方法，使用filter()内置类
        # stu_search_name = filter(lambda stu: stu['name'] == stu_name, students)

        for stu in stu_search_name:
            print('学号:{s_id},姓名:{name},性别:{sex},年龄:{age},☎:{tel}'.format(**stu))

    elif operator == '3':
        stu_id = input('请输入学生ID:')
        stu_search_id = []
        for stu in students:
            if stu['s_id'] == stu_id:
                stu_search_id.append(stu)

        # stu_search_id = filter(lambda stu: stu['s_id'] == stu_id, students)

        if not stu_search_id:
            print('没有找到此id的学生')
        for stu in stu_search_id:
            print('学号:{s_id},姓名:{name},性别:{sex},年龄:{age},☎:{tel}'.format(**stu))
    else:
        pass


def modify_student():
    pass


def delete_student():
    pass


def show_manager(file_name):
    # with open(base_dir + file_name, 'r', encoding='utf8') as file:
    #     while True:
    #         content = file.read() % name
    #         print(content)

    # 调用file_manager模块里的read_file方法
    content = file_manager.read_file(file_name) % name
    while True:
        print(content)
        operator = input('请选择(1~5):')
        if operator == '1':
            add_student()
        elif operator == '2':
            show_student()
        elif operator == '3':
            modify_student()
        elif operator == '4':
            delete_student()
        elif operator == '5':
            break
        else:
            print('您输入的内容有误，请重新输入')
