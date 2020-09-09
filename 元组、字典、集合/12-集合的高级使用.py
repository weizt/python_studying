first = {'李白', '白居易', '李清照', '杜甫', '王昌龄', '王维', '孟浩然', '王安石'}
second = {'李商隐', '杜甫', '李白', '白居易', '岑参', '王昌龄'}
third = {'李清照', '刘禹锡', '岑参', '王昌龄', '苏轼', '王维', '李白'}

# set 支持多种运算符
# set不支持加法+运算
# set支持减法运算
print(first - second)  # A-B,求A和B的差集
# set支持和运算
print(first & second)  # A&B,求A和B的交集
# set 支持或运算
print(first | second)  # A|B,求A和B的并集
# set支持异或运算
print(first ^ second)  # A^B,求A和B的差集的并集
