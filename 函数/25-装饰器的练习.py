# 需求：权限验证

# 权限值相加，得到的值就是用户所拥有的权限 ，如6=4+2，则拥有读写权限
# 用二进制来判断用户的权限关系
user_permission = 6  # 用户权限 0110

DELETE_PERMISSION =8 # 删除权限 1000  从右起第四位有1表示read权限
READ_PERMISSION = 4  # 读取权限 0100  从右起第三位有1表示read权限
WRITE_PERMISSION = 2  # 写入权限 0010  从右起第二位有1表示write权限
EXE_PERMISSION = 1  # 执行权限 0001  从右起第一位有1表示exe权限


# 定义装的器函数，需要2个参数
def check_permission(x, y):
    print(x, y)

    def handle_action(fn):
        pass

        def do_action():
                fn()

        return do_action

    return handle_action


# 执行装饰品函数
@check_permission(user_permission, READ_PERMISSION)
def read():
    print('我在读取内容')


@check_permission(user_permission, WRITE_PERMISSION)
def wirte():
    print('我在写入内容')


@check_permission(user_permission, EXE_PERMISSION)
def exe():
    print('我在执行内容')

def delete():
    print('我正在删除文件')


read()
wirte()
exe()
delete()