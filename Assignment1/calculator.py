import click
'import math'

@click.group()
def cli():
    pass

@cli.command()
@click.option('--num', type=int)
def absv(num):
    'Calculates absolute value.'
    click.echo('absolute value = {}'.format(abs(num)))

@cli.command()
@click.argument('n1', type=int)
@click.argument('n2', type=int)
def add(n1, n2):
    'Adds two integers.'
    click.echo('sum = {}'.format(n1 + n2))

@cli.command()
@click.argument('n1', type=int)
@click.argument('n2', type=int)
@click.option('--i', is_flag=True, help='Force integer division')
def divide(n1, n2, i):
    'Divides two integers (N1/N2). To force integer division, use --i option.'
    try:
        if i:
            click.echo('division = {}'.format(n1 // n2))
        else:
            click.echo('division = {}'.format(n1 / n2))

    except ZeroDivisionError:
        click.echo('Error: cannot divide by zero')

@cli.command()
@click.argument('n1', type=int)
@click.argument('n2', type=int)
def multiply(n1, n2):
    'Multiplies two integers.'
    click.echo('result = {}'.format(n1 * n2))

@cli.command()
@click.argument('n1', type=int)
@click.argument('n2', type=int)
def subtract(n1, n2):
    'Subtracts two integers.'
    click.echo('result = {}'.format(n1 - n2))

if __name__ == '__main__':
    cli()
