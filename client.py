# for python 2.x
from socket import *
import time

class socket_helper:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

    def connect(self):
        self.s = socket()
        self.s.connect((self.HOST, self.PORT))

    def send_message(self, data):
        self.s.sendall(str(data))

    def receive_message(self, buffer_size = 1024):
        temp = self.s.recv(buffer_size)
        self.s.close()
        return temp


HOST = '127.0.0.1'
PORT = 65432

s = socket_helper(HOST, PORT)

for i in range(10):
    s.connect()
    s.send_message(i)
    print(s.receive_message(1024))
    time.sleep(2)

