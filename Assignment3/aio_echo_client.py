import asyncio
import aioconsole
import threading

g_msgs = asyncio.Queue()

async def handle_user_input():
    while True:
        msg = await aioconsole.ainput('{} - enter a message'.format(threading.current_thread().getName()))
        await g_msgs.put(msg)

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, loop, msgs):
        self.loop = loop
        self.msgs = msgs

    async def send_forever(self):
        while True:
            msg = await g_msgs.get()
            self.transport.write(msg.encode())
            print('{} - data sent: {}'.format(threading.current_thread().getName(), msg))

    def connection_made(self, transport):
        self.transport = transport

        # Any of below approaches will kick start the coroutine
        #asyncio.ensure_future(self.send_forever())
        #asyncio.create_task(self.send_forever())
        self.loop.create_task(self.send_forever())

    def data_received(self, data):
        print('{} - data received: {}'.format(threading.current_thread().getName(), data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()


loop = asyncio.get_event_loop()

connect_coro_obj = loop.create_connection(lambda: EchoClientProtocol(loop, g_msgs), '127.0.0.1', 8080)
user_interface_coro_obj = handle_user_input()

loop.create_task(connect_coro_obj)
loop.create_task(user_interface_coro_obj)

try:
    loop.run_forever()
finally:
    print('{} - closing main event loop'.format(threading.current_thread().getName()))
    loop.close()
