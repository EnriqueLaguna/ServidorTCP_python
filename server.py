# echo python.py

import socket

HOST = "127.0.0.1" # Localhost
PORT = 65432 # Un puerto no privilegiado


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024)
            print(f'Data received: {data}')
            if not data:
                break
            conn.sendall(data)