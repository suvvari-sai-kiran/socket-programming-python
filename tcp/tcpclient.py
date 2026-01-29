import socket

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(("127.0.0.1", 5000))
print("Connected to server")

try:
    while True:
        payload = input("Enter message (type END to quit): ")
        client_socket.send(payload.encode("utf-8"))

        if payload.strip().upper() == "END":
            break

        data = client_socket.recv(1024)
        print("Received from server:", data.decode("utf-8"))

except KeyboardInterrupt:
    print("\nExited by user")

client_socket.close()
print("Client socket closed")
