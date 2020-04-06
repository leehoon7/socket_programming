# for python 2.x
from socket import *
import pickle
import numpy as np

class socket_helper:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

    def connect(self):
        self.s = socket()
        self.s.connect((self.HOST, self.PORT))

    def send_message(self, data):
        self.s = socket()
        self.s.connect((self.HOST, self.PORT))
        self.s.sendall(pickle.dumps(data, protocol=2))

    def receive_message(self, buffer_size = 1024):
        temp = pickle.loads(self.s.recv(buffer_size))
        self.s.close()
        return temp

class communicator:
    def __init__(self, socket):
        self.s = socket

    def initialization(self):
        self.s.send_message(['i'])
        return 'i' == self.s.receive_message()

    def send_state(self, state):
        self.s.send_message(['s', state])
        self.s.receive_message()

    def get_action(self):
        self.s.send_message(['a'])
        return self.s.receive_message()

    def send_reward(self, reward):
        self.s.send_message(['r', str(reward)])
        self.s.receive_message()

    def termination(self):
        self.s.send_message(['t'])
        self.s.receive_message()

    def finish(self):
        self.s.send_message(['f'])
        return self.s.receive_message()

if __name__ == "__main__":

    import time

    HOST = '127.0.0.1'
    PORT = 65432

    episode = 2
    t = 5

    s = socket_helper(HOST, PORT)
    com = communicator(s)
    start = 0

    if com.initialization():
        start = time.time()
        for i in range(episode):
            print('episode ' + str(i+1) + ' start..')

            for j in range(t):
                print('  time: ' + str(j+1))

                com.send_state([i+1, j+1])

                if j % 2 == 0:
                    com.get_action()

                if j == t - 1 :
                    com.termination()

                time.sleep(0.1)

            if i == episode - 1 :
                print(com.finish())

        print('************')
        print('all finished')
        print('total time : '+str(time.time() - start))
        print('************')

        print('***** test *****')
        com.s.send_message(['check_for_various_type', 123123, 0.123123, np.array([1, 2, 3])])

    else :
        print('************')
        print('error')
        print('************')