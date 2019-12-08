import socket


class Client:
    def connect(self, host, port, i):
        try:
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
                while True:
                    while True:
                        message = input()
                        s.send(message.encode('utf-8'))
                        if message.endswith('.') or message == 'quit':
                            break
                    if message == 'quit':
                        break
                    data = s.recv(2000)
                    print('Got back: {}'.format(data.decode('utf-8')))
                s.shutdown(socket.SHUT_WR)
                data = s.recv(2000)
                s.shutdown(socket.SHUT_RD)
                s.close()
                print('Got back: {}'.format(data.decode('utf-8')))
        except:
            print('Cannot make a connection to the server. Please make sure the server is running.')

