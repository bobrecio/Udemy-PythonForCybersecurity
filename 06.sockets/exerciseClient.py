import socket

# 1. socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. connect
host = '127.0.0.1'
port = 9001

s.connect((host, port))

# client recieves; b/c server is sending
while True:
    msg = s.recv(1024).decode()
    if not msg:
        break
    print(f"server > {msg}")
    data = input("Enter a message to the server >> ")
    s.sendall(str.encode(data))

s.close
print(f"Connection closed")
