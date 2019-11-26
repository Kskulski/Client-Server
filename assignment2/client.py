import socket


class Client:
    def connect(self, host, port, i):
        remote_server = (host, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(remote_server)
        if not i:
            while True:
                message = input()
                s.send(message.encode('utf-8'))
                if message.endswith('.'):
                    break
            s.shutdown(socket.SHUT_WR)
            data = s.recv(2000)
            s.shutdown(socket.SHUT_RD)
            s.close()
            print('Got back: {}'.format(data.decode('utf-8')))
        if i:
            while input() != 'quit':
                while True:
                    message = input()
                    s.send(message.encode('utf-8'))
                    if message.endswith('.'):
                        break
                data = s.recv(2000)
                print('Got back: {}'.format(data.decode('utf-8')))
            s.shutdown(socket.SHUT_WR)
            data = s.recv(2000)
            s.shutdown(socket.SHUT_RD)
            s.close()
            print('Got back: {}'.format(data.decode('utf-8')))


