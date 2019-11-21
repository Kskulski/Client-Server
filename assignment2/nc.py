import click
from client import Client
from server import Server

@click.group()
def cli():
    pass

@cli.command()
@click.argument('host', default='127.0.0.1')
@click.argument('port', type=int, default=8080)
@click.option('--i', is_flag=True, help='Interactive mode')
def connect(port, host, i):
    """Connects to a TCP server on HOST PORT. Defaults to localhost 8080"""
    Client.connect(host, port, i)
    click.echo('Connecting to {}:{}'.format(host, port))


@cli.command()
@click.option('--port', type=int, default=8080)
def listen(port):
    """Runs in server mode and listens on port --port."""
    server = Server()
    server.listen(port)
    click.echo('Starting server onport: {}'.format(port))

if __name__ == '__main__':
    cli()
