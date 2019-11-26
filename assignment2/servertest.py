import socket
import threading


class Server:
    def listen(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', port))
        s.listen(1)
        while True:
            conn, remote_addr = s.accept()
            print('[+] connection from {}'.format(remote_addr))
            #chunks = []
            while True:
                chunks = []
                    while True:
                    data = conn.recv(2000)
                    if not data:
                        break
                    chunks.append(data.decode('utf-8'))
                    message = ''.join(chunks)
                    self.data_received(conn, data, remote_addr, message)
                    chunks.append(' ')
            conn.send('Good Bye!'.encode('utf-8'))
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
            break
        #threading.Timer(120)
        #print('Server shutting down. Good Bye!')

    def data_received(self, conn, data, remote_addr, message):
        if data.decode('utf-8').endswith('.'):
            print('received {} from  {}'.format(message, remote_addr))
            conn.send('Echo: {}'.format(message).encode('utf-8'))