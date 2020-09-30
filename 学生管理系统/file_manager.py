# 定义一个文件打开函数，用作模块调用

base_dir = './files/'


def read_file(file_name):
    try:
        with open(base_dir + file_name, 'r', encoding='utf8') as file:
            while True:
                content = file.read()
                return content
    except FileNotFoundError:
        print('文件未找到')
