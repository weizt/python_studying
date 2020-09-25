import csv

# CSV文件的写入
file = open('demo.csv', 'w', encoding='utf8', newline='')  # newline=''表示中间不加空行

info = csv.writer(file)

# 第一种以单行的形式写入
info.writerow(['name', 'age', 'score', 'city'])
info.writerow(['zhangsan', '16', '89', '上海'])
info.writerow(['lisi', '20', '90', '北京'])



# 第二种以多行的形式写入
info.writerows([
    ['姓名', '年龄', '分数', '城市'],
    ['marry', 33, 99, '海南'],
    ['jack', 31, 90, '南京']
])

# CSV文件的读取
file = open('info.csv', encoding='utf8', newline='')
r = csv.reader(file)
for date in r:
    print(date)
