import socket

# socket功能：1.不同电脑之间的网络通信需要使用socket
#            2.在同一台电脑中不同的程序之间进行通信
# socket三步骤：
# 1.创建socket并连接
# AF_INET:表示这个socket是用来进行网络连接
# SOCK_DGRAM:表示连接是一个UDP连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定一个本地主机的IP地址和端口号，则既可以发送，也可以接收
s.bind(('192.168.21.107', 9091))

# 2.发送数据
# data:要发送的数据内容，是一个二进制数据
# address:发送的目标地址，参数是一个元组，分别写目标IP主机的地址和目标程序的端口号
s.sendto('你好，我是外星人！'.encode(encoding='utf8'), ('192.168.21.107', 9090))  # sendto()方法需要两个参数:data;address

# 3.接收消息
data, addr = s.recvfrom(1024)
print('来自{}端口号{}发来了消息，内容是:{}'.format(addr[0], addr[1], data.decode(encoding='utf8')))

# 4.关闭socket
s.close()
