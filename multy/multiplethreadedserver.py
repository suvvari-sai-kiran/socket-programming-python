import socket
from _thread import start_new_thread

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 5000
Threadcount = 0

serversocket.bind((host, port))
serversocket.listen(5)

print("Server waiting for connections...")

def client_thread(connection):
    connection.send("Welcome to the server\n".encode())

    while True:
        data = connection.recv(1024)
        if not data:
            break
        reply = "Server output: " + data.decode()
        connection.sendall(reply.encode())

    connection.close()

while True:
    conn, addr = serversocket.accept()
    print("Connected to:", addr)
    start_new_thread(client_thread, (conn,))
    Threadcount += 1
    print("Thread Number:", Threadcount)

serversocket.close()
