import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 5000))

print("UDP Server is running...")

while True:
    data, addr = sock.recvfrom(1024)
    print("Received message:", data.decode())

    message = "Hello from UDP server"
    sock.sendto(message.encode(), addr)
    print("Sent response to:", addr)
