import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('n1', type=int)
@click.argument('n2', type=int)
@click.option('--i', is_flag=True)
def divide(n1, n2, i):
    try:
        if i:
            click.echo('result = {}'.format(n1 // n2))
        else:
            click.echo('result = {}'.format(n1 / n2))

    except ZeroDivisionError:
        click.echo('cannot divide by zero')


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
