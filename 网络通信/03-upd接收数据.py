import socket

# 创建一个基于UDP的网络socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口号和IP地址,参数是一个元组
s.bind(('192.168.21.107', 9090))

# recvfrom()方法接收数据,接收到的是一个元组：
# 第0个元素是发送端发送的数据；第1个元素是发送端的IP地址和端口号
# content = s.recvfrom(1024) # recvfrom()是一个阻塞方法，一直处于等待状态
# x = content[0].decode(encoding='utf8')
data, addr = s.recvfrom(1024)  # 把接收的元组进行拆包，ip,端口 == addr; 数据==data
print('从{}地址{}端口号接收到了消息：{}'.format(addr[0], addr[1], data.decode(encoding='utf8')))

# 关闭socket连接
s.close()
