import threading
import asyncio
from time import sleep
class EchoProtocolHandler(asyncio.Protocol):

    async def blocking_call(self):
        print('{} - going to sleep'.format(threading.current_thread().getName()))
        await asyncio.sleep(3)
        print('{} - done sleeping'.format(threading.current_thread().getName()))

    def connection_made(self, transport):
        """Called on new client connections"""
        self._transport = transport
        self._remote_addr = transport.get_extra_info('peername')
        print('[+] connection from {}'.format(self._remote_addr))
        self._pieces = []

    def data_received(self, data):
        "Handle data"
        print('received {}'.format(data.decode('utf-8')))
        self._pieces.append(data.decode('utf'))

        if ''.join(self._pieces).endswith('.'):
            self._transport.write(''.join(self._pieces).encode('utf-8'))

        asyncio.ensure_future(self.blocking_call())


    def connection_lost(self, exc):
        print('[-] lost connection to {}'.format(self._remote_addr))
        self._transport.close()


e_loop = asyncio.get_event_loop()
corouting = e_loop.create_server(EchoProtocolHandler,
                                 host='0.0.0.0',
                                 port=8080)

server = e_loop.run_until_complete(corouting)
e_loop.run_forever()



