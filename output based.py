import socket
import sys

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Socket creation failed")
    print("Reason:", err)
    sys.exit()

print("Socket created")

target_host = input("Enter the host IP: ")
target_port = int(input("Enter the port number: "))

try:
    sock.connect((target_host, target_port))
    print(f"Socket connected to {target_host}:{target_port}")
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
except socket.error as err:
    print(f"Connection error to {target_host}:{target_port}")
    print("Reason:", err)
    sys.exit()
