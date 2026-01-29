import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "Hello UDP server"
sock.sendto(msg.encode("utf-8"), ('127.0.0.1', 5000))

data, addr = sock.recvfrom(1024)
print("Server says:", data.decode())

sock.close()
