import socket

# 基本tcp协议的socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 在发送数据之前必须调用connect()方法，与服务器建立连接
s.connect(('192.168.21.107', 9797))

# 调用send()方法直接发送消息到目标主机
s.send('你好，我是外星人！'.encode('utf8'))

# 关闭socket
s.close()
