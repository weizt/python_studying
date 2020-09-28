# with关键字：我们称之为上下文管理器，很多需要手动关闭的连接都可以用with关键自动关闭
# 比如说：文件连接、socker连接、数据库的连接都能使用with关键字关闭连接
# with关键字后面的对象，必须要实现__enter__ 和 __exit__魔法方法

try:
    with open('name.txt', 'r', encoding='utf8') as file:
        x = file.read()
        print(x)
        # file.close() 不需要再手动关闭文件了，with关键字会自动帮我们关闭文件
except FileNotFoundError:
    print('文件未找到')
