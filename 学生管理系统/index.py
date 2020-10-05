# 基础结构的搭建和退出功能的实现
# 定义一个函数，用来读取welcome.txt，显示主页
import sys

import file_manager

import model


# 先定义一个空字典，把老师添加到这个字典里,这个字典不能默认为空
# date = {}


# 注册功能的实现
def register():
    # 读取文件，查看文件中有没有数据
    date = file_manager.read_json('date.json', {})

    while True:
        teacher_name = input('请输入您的用户名:(3~12位)')
        if not 3 <= len(teacher_name) <= 12:
            print('用户名不符合要求，请重新输入')
        else:
            break

    while True:
        password = input('请输入您的密码:(6~12)')
        if not 6 <= len(password) <= 12:
            print('您输入密码有误，请重新输入')
        else:
            break
    # 用户密码都已经输入正确以后，创建一个teacher对象
    t = model.Teacher(teacher_name, password)
    date[t.name] = t.password
    # date[teacher_name] = password
    # print(teacher)
    file_manager.write_json('date.json', date)


# 登陆功能的实现
def login():
    pass


def start():
    content = file_manager.read_file('welcome.txt')
    while True:
        operator = input(content + '请输入需要操作的数字(1-3):')
        if operator == '1':
            print('登陆')
        elif operator == '2':
            register()
        elif operator == '3':
            # break
            sys.exit(0)
        else:
            print('请输入正确的数字')


if __name__ == '__main__':
    start()
