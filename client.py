# echo-client.py

import nacl.utils
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def generateRandomNumber() -> str: 
    num_bytes = nacl.utils.random(3)
    random_number = int.from_bytes(num_bytes, "big", signed=False)
    return str(random_number)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(generateRandomNumber().encode())
    data = s.recv(1024)

print(f"Received {data!r}")
