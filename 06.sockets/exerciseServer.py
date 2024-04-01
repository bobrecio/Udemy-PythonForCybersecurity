import socket

# 1. socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. bind
host = '127.0.0.1'
port = 9001
s.bind((host, port))  # port should be higher than 1024

# 3. listen
print(f"Listening on port {port}")
s.listen()

# 4. accept
client, addr = s.accept()

# when someone connects
# print(f"Connection from {addr}")
server_pwd = "Test1234"
pwd_prompt = f"Send back this password: {server_pwd}"

client.sendall(str.encode(pwd_prompt))  # send the prompt

client_pwd = client.recv(1024).decode()  # get the password

while client_pwd == server_pwd:
    data = input("Enter a message to the client >> ")
    client.sendall(str.encode(data))
    msg = client.recv(1024).decode()
    if not msg:
        break
    print(f"client > {msg}")

client.close()
print(f"Connection with {addr} has closed")
