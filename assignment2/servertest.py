import socket


class Server:
    def listen(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', port))
        s.listen(1)
        while True:
            conn, remote_addr = s.accept()
            print('[+] connection from {}'.format(remote_addr))
            while True:
                chunks = []
                while True:
                    data = conn.recv(2000)
                    if not data or data.decode('utf-8') == 'quit':
                        break
                    chunks.append(data.decode('utf-8'))
                    message = ''.join(chunks)
                    end = self.data_received(conn, remote_addr, message)
                    if end:
                        break
                    chunks.append(' ')
                if not data or data.decode('utf-8') == 'quit':
                    break
            conn.send('Good Bye!'.encode('utf-8'))
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
            break
        print('Server shutting down. Good Bye!')

    def data_received(self, conn, remote_addr, message):
        if message.endswith('.'):
            print('received: {} from {}'.format(message, remote_addr))
            conn.send('Echo: {}'.format(message).encode('utf-8'))
            return True
        else:
            return False