import os
import socket

# 1.创建服务端socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.绑定本机的IP和端口号
server_socket.bind(('192.168.21.107', 9797))

# 3.让服务器处于监听状态，超过服务端并发数后，队列数为128个
server_socket.listen(128)

# 4.识别客户端的信息
client_socket, client_addr = server_socket.accept()

# 5.接收客户端的请求，并把客户的请求保存到data中
data = client_socket.recv(1024).decode('utf8')

# 使用二进制的形式读取客户端请求的文件并发送文件到客户端
if os.path.isfile(data):
    print('文件已下载，并返回给客户端')
    with open(data, 'rb') as file:
        content = file.read()
        client_socket.send(content)
else:
    print('文件不存在')
