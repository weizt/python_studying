import socket

# 基本tcp协议的socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务器地址和端口号
s.bind(('192.168.21.107', 9797))

# 把socket变成一个被动监听的socket
s.listen(128)  # 128指队列数：如极限处理数为1000，有1120个用户，则120处于128的队列当中，超过队列数则提示连接失败

# 接收客户端的请求
# accept()方法接收数据,接收到的是一个元组：
# 第0个元素是客户端scoket数据；第1个元素是客服端的IP地址和端口号
client_socket, client_addr = s.accept()

# tcp里使用recv()方法接收数据，每次接收1024个字节
data = client_socket.recv(1024)

# 输入客户端的信息和发送的内容
print('接收到{}客户端{}端口号的发送的数据，数据内容是:{}'.format(client_addr[0], client_addr[1], data.decode('utf8')))
