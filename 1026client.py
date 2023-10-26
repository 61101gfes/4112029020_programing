import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 3000)
client_socket.connect(server_address)

try:
    
    length = int(input("請輸入費氏數列長度: "))

    
    client_socket.sendall(str(length).encode())

    
    data = client_socket.recv(1024)
    print("伺服器回應:", data.decode())

finally:
    
    client_socket.close()