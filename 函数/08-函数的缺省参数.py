# 函数的默认参数的使用
# print函数中end=''就是一个缺省参数
# 如果没有传递参数，就使用默认的值
print('hello world', end='\t')
print()


# 缺省参数必须写在后面
def say_hellop(name, age, city='东夏'):  # 形参city设置为一个缺少值
    print('大家好，我是{}，我今年{}，我来自{}'.format(name, age, city))


say_hellop('weizhetao', 19)
# 传参的方式有多种，可以使用变量赋值（关键字参数）的形式传参
say_hellop(name='weizhetao', age=19, city='郎溪')
# 如果有位置参数和关键字参数，关键字参数一定要放在位置参数的后面
say_hellop('weizhetao', age=19, city='郎溪')
