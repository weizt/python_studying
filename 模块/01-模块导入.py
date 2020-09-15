# 概念：在python中一个py文件，就可以理解为一个模块
# 不是所有的py文件都能作为模块，如果想让py文件作为模块导入，模块名字必须要遵守命名规则
# 导入模块方法，python提供了很多内置模块

import time

# 1.使用import + 模块名 直接导入一个模块
# 使用此导入方式，调用方法时要加 （模块名.方法名）
# 导入这个模块以后，就可以使用这个模块里的方法和变量
print(time.time())

from random import randint

# 2. from 模块名 import 函数名，导入一个模块里的方法或变量
randint(0, 2)  # 生成[0，2]的随机整数，不能使用random.randint()，因我们没有导入random模块，而是导入了random里的一个方法

from math import *

# 3.from 模块名 import * 导入这个模块里的‘所有’方法和变量
print(pi)  # 不需要使用math.pi

import datetime as dt  #

# 4.导入一个模块并给这个模块起一个别名
print(dt.MAXYEAR)

from copy import deepcopy as dp

# 5. from 模块名 import 函数名 as 别名，引入一个模块中的函数并起一个别名
print(dp(['hello', 'ok', [1, 2, 3], 'good']))
