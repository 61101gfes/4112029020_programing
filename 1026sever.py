import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 3000)
server_socket.bind(server_address)


server_socket.listen(1)
print("等待客戶端連接...")


client_socket, client_address = server_socket.accept()
print("已連接到客戶端:", client_address)

try:
    while True:
        
        data = client_socket.recv(1024)
        if not data:
            break

        
        length = int(data.decode())
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < length:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)

        response = ", ".join(map(str, fibonacci_sequence))
        client_socket.sendall(response.encode())

finally:
    
    client_socket.close()
    server_socket.close()