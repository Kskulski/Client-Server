import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0', 8080))
s.listen(20)

while True:
    conn, remote_addr = s.accept()
    print('[+] connection from {}'.format(remote_addr))

    chunks = []
    while True:
        data = conn.recv(2000)
        if not data:
            break

        chunks.append(data.decode('utf-8'))

    message = ''.join(chunks)

    print('received {} from  {}'.format(message, remote_addr))

    conn.send('Echo: {} - Good Buy!'.format(message).encode('utf-8'))
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

