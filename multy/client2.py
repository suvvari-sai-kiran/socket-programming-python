import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 5000

clientsocket.connect((host, port))

while True:
    server_msg = clientsocket.recv(1024)
    if not server_msg:
        break
    print("Client-2 received:", server_msg.decode())

    msg = input("Client-2 message: ")
    if msg.lower() == "exit":
        break
    clientsocket.sendall(msg.encode())

clientsocket.close()
