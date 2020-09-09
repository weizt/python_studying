# 这个变量是全局变量，在整个py文件里都可以访问
# 在python,只有函数能够分割作用域
a = 100
word = '你好'


# 这个变量是在函数内部定义的变量，它是局部变量，只能在函数内部使用
def test():
    x = 'hello'
    print('x={}'.format(x))
    # 如果局部变量和全局变量同名，会在函数内部又定义了一个新的局部变量
    a = 10
    print('函数内部a={}'.format(a))
    # 如果使用global对变量进行声明，可以通过函数修改全局变量的值
    global word
    word = 'hello'  # 在函数内部修改全局变量

    # 使用globals()和locals()查找全局变量和局部变量
    print('locals={},globals+{}'.format(locals(), globals()))


test()

print('函数外部的word是:{}'.format(word))
