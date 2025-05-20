import socket

HOST = '127.0.0.1'
PORT = 6666

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen() # create a listening socket for new connections
    print(f'listening on {HOST}:{PORT}')
    conn, addr = s.accept() # when a client connects, the server creates a new socket for writing
    # while the new socket exsists:
    with conn:
        print(f'Connected to {addr}') # print clients address
        while True:
            data = conn.recv(1024) # fetch clients data
            print(f'Received {data}') # print on terminal
            if not data:
                break #If conn.recv() returns an empty bytes object, b'', that signals that the client closed the connection 
            conn.sendall(data) # echo data back to client