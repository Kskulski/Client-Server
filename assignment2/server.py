import socket


class Server:
    def listen(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', port))
        s.listen(20)
        while True:
            conn, remote_addr = s.accept()
            print('[+] connection from {}'.format(remote_addr))
            chunks = []
            while True:
                data = conn.recv(2000)
                if not data:
                    break
                while True:
                    chunks.append(data.decode('utf-8'))
                    if data.decode('utf-8').endswith('.'):
                        break
                    data = conn.recv(2000)
                    #if not data:
                     #   break

                message = ''.join(chunks)
                print('received {} from  {}'.format(message, remote_addr))
                conn.send('Echo: {} - Good Buy!'.format(message).encode('utf-8'))

                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
                break