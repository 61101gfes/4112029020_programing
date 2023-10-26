import socket

# 创建服务器 socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务器到 IP 地址和端口
server_address = ('localhost', 3000)
server_socket.bind(server_address)

# 监听客户端连接
server_socket.listen(1)
print("等待客戶端連接...")

# 接受客户端连接
client_socket, client_address = server_socket.accept()
print("已連接到客戶端:", client_address)

try:
    while True:
        # 接收客户端发送的数据
        data = client_socket.recv(1024)
        if not data:
            break

        # 将接收的数据作为斐波那契数列的长度
        length = int(data.decode())
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < length:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)

        response = ", ".join(map(str, fibonacci_sequence))
        client_socket.sendall(response.encode())

finally:
    # 关闭连接
    client_socket.close()
    server_socket.close()