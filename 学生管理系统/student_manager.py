base_dir = './files/'
name = ''


def show_manager(file_name):
    with open(base_dir + file_name, 'r', encoding='utf8') as file:
        while True:
            content = file.read() % name
            print(content)
            input('请选择(1~5):')
