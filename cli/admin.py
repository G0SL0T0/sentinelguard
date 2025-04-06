import click
from core.actions import isolate_host
from core.host_scanner import scan_host

@click.group()
def cli():
    pass

@cli.command()
@click.argument("ip")
def scan(ip):
    scan_host(ip)
    click.echo(f"Сканирование {ip} завершено")

@cli.command()
@click.argument("ip")
def isolate(ip):
    isolate_host(ip)
    click.echo(f"Хост {ip} изолирован")

if __name__ == "__main__":
    cli()