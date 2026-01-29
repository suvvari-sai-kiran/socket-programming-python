import socket
import threading
from queue import Queue

target = "172.16.2.6"
queue = Queue()
open_port = []

# Fixed typo: should be AF_INET, not AF_INT
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Optional: Set timeout to avoid hanging
        sock.connect((target, port))
        sock.close()
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f"Port {port} is open!")
            open_port.append(port)
        queue.task_done()

# Fill queue with port numbers 1 to 1023
port_list = range(1, 1024)
fill_queue(port_list)

# Create 100 threads
thread_list = []
for _ in range(100):
    thread = threading.Thread(target=worker)  # Fixed threading call
    thread_list.append(thread)

# Start all threads
for thread in thread_list:
    thread.start()

# Wait for all threads to complete
for thread in thread_list:
    thread.join()

print("Open ports are:", open_port)
