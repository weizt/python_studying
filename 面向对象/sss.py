# x = 0
# for i in range(0, 11):
#     x += i
#     print(x)
flog = True
while flog:
    stu_name = input('请输入学生的姓名：')
    while True:
        choice = input('添加成功！\n1.继续\n2.返回\n请选择(1~2):')
        if choice == '2':
            flog = False
            break
        elif choice == '1':
            continue
        else:
            print('输入有误，请重新输入')
