# 一个模块本质上就是一个py文件
# 自己定义一个模块，其实就是自己写一个py文件
# 模块要求
'''
1.文件名一定要遵守规范。由数字、字母和下划线组成，不能用数字开头
2.使用from <module_name> import *方法时，导入这个模块里’所有‘的变量和函数
  本质上是读取模块里的__all__属性，看这个属性里定义了哪些变量和函数
  如果这个模块里没有用__all__才会导入所有不_开头的变量和函数
  没有设置__all__会读取除了以_开的的所有变量和函数
3.在模块中以一个下划线开始的变量，是一个私有变量，外部无法调用
  如果非要导入，可以使用import module_name，调用时，用modulo_nmae._变量名的方式
  在模块里加 del _变量名，外部无法调用
  以一个下划线开始的变量，建议只在本模块里使用，别的模块不要导入
'''

# 举例说明
# 假设模块里定义了3个变量，2个函数
# 同时设定了__all__变量
# 外部使用 from <module_name> import * 方法调用本模块的变量或函数时，只能调用__all__列表里的值
# 如果import <module_name> 方法调用模块，只可以绕开这个限定
__all__ = ['a', 'b', 'test'] # 相当于做了限定，列表里有才能用，没有就不能用

a = 'hello'
b = 1 + 1
c = 100


def foo(x, y):
    return x + y


def test():
    print('我是函数test()')
