# 基础结构的搭建和退出功能的实现
# 定义一个函数，用来读取welcome.txt，显示主页


import file_manager


def start():
    content = file_manager.read_file('welcome.txt')
    while True:
        operator = input(content + '请输入需要操作的数字(1-3):')
        if operator == '1':
            print('登陆')
        elif operator == '2':
            print('注册')
        elif operator == '3':
            break
        else:
            print('请输入正确的数字')


if __name__ == '__main__':
    start()
