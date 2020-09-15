# 使用pip安装包
pip install <package_name>

# 使用pip卸载包
pip uninstall <package_name>

# 列出当前环境安装了哪些模块
pip list

# 列出所有模块和版本
pip freeze
# 在终端重定向第三方包输出到指定的文件
# pip freeze > <file_name>
pip freeze > requirements.txt
# 读取指定文件里的文件名和版本号并安装
pip install -r file_name

# 从指定路径下载第三方包（临时修改）
pip install <package> -i <url>

# 永久修改国内下载源
# 注：windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini。

# 国内pip源列表：
# 清华：https://pypi.tuna.tsinghua.edu.cn/simple
# 豆瓣：http://pypi.douban.com/simple/
# 阿里云：http://mirrors.aliyun.com/pypi/simple/
# 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/


#添加或者修改为如下内容：
# [global]
# index-url = https://pypi.tuna.tsinghua.edu.cn/simple
# [install]
# trusted-host=mirrors.aliyun.com
