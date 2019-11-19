import click
from client.py import Client

@click.group()
def cli():
    pass

@cli.command()
@click.argument('host', default='127.0.0.1')
@click.argument('port', type=int, default=8080)
@click.option('--i', type=bool, default=False)
def connect(port, host):
    click.echo('connecting to {}:{}'.format(host, port))

@cli.command()
@click.option('--port', type=int, default=8080)
def listen(port):
    click.echo('starting server onport: {}'.format(port))

if __name__ == '__main__':
    cli()
