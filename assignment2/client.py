import socket


class Client:
    def connect(self, host, port, i):
        remote_server = (host, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(remote_server)
        if not i:
            while True:
                s.send(input().encode('utf-8'))
            s.shutdown(socket.SHUT_WR)
            data = s.recv(2000)
            s.shutdown(socket.SHUT_RD)
            s.close()
            print('Got back: {}'.format(data.decode('utf-8')))
        if i:
            while input() != 'quit':
                message = input()
                s.sendall(message.encode('utf-8'))
                s.shutdown(socket.SHUT_WR)
                data = s.recv(2000)
                s.shutdown(socket.SHUT_RD)
                s.close()
                print('Got back: {}'.format(data.decode('utf-8')))


'''remote_server = ('127.0.0.1', 8080)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(remote_server)
s.sendall('Omari'.encode('utf-8'))
s.shutdown(socket.SHUT_WR)
data = s.recv(2000)
s.shutdown(socket.SHUT_RD)
s.close()
print('Got back: {}'.format(data.decode('utf')))'''
