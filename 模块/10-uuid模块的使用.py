# 用来生成一个全局唯一的id模块
import uuid

print(uuid.uuid1())  # 32个长度，每个字符有16个选择 16**32
