# for python 3.x
import socket

class socket_helper:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

    def server_start(self):
        self.s = socket.socket()
        self.s.bind((self.HOST, self.PORT))
        self.s.listen()
        print("listening :", self.PORT)

    def wait_and_receive(self, buffer_size=1024):
        self.conn, self.addr = self.s.accept()
        print('accepted : connected by', self.addr)
        return self.conn.recv(buffer_size).decode()

    def send_message(self, data):
        self.conn.sendall(data)

HOST = '127.0.0.1'
PORT = 65432

s = socket_helper(HOST, PORT)
s.server_start()
while True:
    msg = s.wait_and_receive()
    #print('received :', msg)
    print(msg[0], msg[1:])

    if msg[0] == 'i':
        pass
    elif msg[0] == 's':
        pass
    elif msg[0] == 'a':
        pass
    elif msg[0] == 't':
        pass
    elif msg[0] == 'f':
        break

    s.send_message(msg.encode())