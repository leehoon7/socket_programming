# for python 3.x
import socket
import pickle
import numpy as np

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
        return pickle.loads(self.conn.recv(buffer_size))

    def send_message(self, data):
        self.conn.sendall(pickle.dumps(data, protocol=2))


if __name__ == "__main__":

    HOST = '127.0.0.1'
    PORT = 65432

    s = socket_helper(HOST, PORT)
    s.server_start()
    while True:
        msg = s.wait_and_receive()
        print('received :', msg)

        if msg[0] == 'i':
            s.send_message('i')

        elif msg[0] == 's':
            s.send_message('s')

        elif msg[0] == 'a':
            s.send_message('a')

        elif msg[0] == 't':
            s.send_message('t')

        elif msg[0] == 'f':
            s.send_message(['check for various type', 123123, 0.123123, np.array([1, 2, 3])])
            msg = s.wait_and_receive()
            print('received :', msg)
            break
