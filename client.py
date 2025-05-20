import socket

HOST = '127.0.0.1'
PORT = 6666
MESSAGE = b'Hello, World!'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #socket.socket creates a TCP socket
    #socket.SOCK_STREAM to use a TCP socket type
    #socket.AF_INET specifies adress family (IPv4)

    s.connect((HOST, PORT))  # double parenthesis because .connect() expects a tupple with two arguments, instead as to sepparate args
    s.sendall(MESSAGE)
    received_message = s.recv(len(MESSAGE))
    print(received_message.decode())