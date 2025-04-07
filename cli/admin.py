import click
from core.host_scanner import scan_host
from core.actions import isolate_host

@click.group()
def cli():
    pass

@cli.command()
@click.argument("ip")
def scan(ip):
    scan_host(ip)
    click.echo(f"[+] Хост {ip} просканирован")

@cli.command()
@click.argument("ip")
def block(ip):
    isolate_host(ip)
    click.echo(f"[+] Хост {ip} заблокирован")

if __name__ == "__main__":
    cli()