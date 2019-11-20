import click
from assignment2.client import
from assignment2.server import

@click.group()
def cli():
    pass

@cli.command()
@click.argument('host', default='127.0.0.1')
@click.argument('port', type=int, default=80)
def connect(port, host):
    click.echo('connecting to {}:{}'.format(host, port))

@cli.command()
@click.option('--port', type=int, default=80)
def listen(port):
    click.echo('starting server onport: {}'.format(port))

if __name__ == '__main__':
    cli()
