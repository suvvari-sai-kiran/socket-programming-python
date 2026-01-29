import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind IP and Port
server_socket.bind(("127.0.0.1", 5000))

# Listen for connections
server_socket.listen(5)
print("Server started and waiting for connections...")

while True:
    client_socket, addr = server_socket.accept()
    print("Client connected from:", addr)

    while True:
        data = client_socket.recv(1024)

        if not data:
            break

        message = data.decode("utf-8")

        if message.strip().upper() == "END":
            print("Client requested to close the connection")
            break

        print("Received from client:", message)

        # Send response to client
        client_socket.send(b"Hey client")

    client_socket.close()
    print("Client connection closed\n")
