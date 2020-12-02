import socket

# 1.创建客户端socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.连接服务器IP
client_socket.connect(('192.168.21.107', 9797))

# 3.输入需要下载载的文件名，并发送给服务器
file_name = input('请输入您要下载的文件名：')
client_socket.send(file_name.encode('utf8'))

# 4.接收服务器回传的数据并保存到data中
# data = client_socket.recv(1024)

# 5.把服务器的返回的文件以二进制的形式不停的写入到文件中，文件名与输入的文件名相同
with open(file_name, 'wb') as file:
    while True:
        data =client_socket.recv(1024)
        if not data:
            break
        file.write(data)

# 6.关闭socket
client_socket.close()
