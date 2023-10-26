import socket

# 创建客户端 socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
server_address = ('localhost', 3000)
client_socket.connect(server_address)

try:
    # 获取用户输入的斐波那契数列长度
    length = int(input("請輸入費氏數列長度: "))

    # 发送数据到服务器
    client_socket.sendall(str(length).encode())

    # 接收服务器的响应
    data = client_socket.recv(1024)
    print("伺服器回應:", data.decode())

finally:
    # 关闭连接
    client_socket.close()