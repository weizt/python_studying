def test(a):
    print('修改前的a的内存地址0x%X' % id(a))
    a = 100
    print('修改后的a的内存地址0x%X' % id(a))


x = 1
print('调用前的x的内存地址0x%X' % id(x))
test(x)
print('调用后的x的内存地址0x%X' % id(x))
print(x)
