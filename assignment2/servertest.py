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
            while True:
                data = conn.recv(2000)
                if not data:
                    break
                self.data_received(conn, data, remote_addr)
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
            break
        #threading.Timer(120)
        #print('Server shutting down. Good Bye!')

    def data_received(self, conn, data, remote_addr):
        chunks = []
        if data.decode('utf-8').endswith('.'):
            chunks.append(data.decode('utf-8'))
            message = ''.join(chunks)
            print('received {} from  {}'.format(message, remote_addr))
            conn.send('Echo: {}'.format(message).encode('utf-8'))
        else:
            data = conn.recv(2000)
            chunks.append(data.decode('utf-8'))