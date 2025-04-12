import click
from core.host_scanner import scan_host
from core.actions import isolate_host
import ipaddress

def validate_ip(ctx, param, value):
    try:
        ipaddress.ip_address(value)
        return value
    except ValueError:
        raise click.BadParameter(f"Некорректный IP: {value}")

@click.group()
def cli():
    """CLI для управления SentinelGuard."""
    pass

@cli.command()
@click.argument("ip", callback=validate_ip)
def scan(ip):
    """Сканирование хоста на уязвимости."""
    try:
        scan_host(ip)
        click.secho(f"[✓] Хост {ip} просканирован", fg="green")
    except Exception as e:
        click.secho(f"[×] Ошибка: {e}", fg="red")

@cli.command()
@click.argument("ip", callback=validate_ip)
def block(ip):
    """Блокировка хоста."""
    if click.confirm(f"Заблокировать хост {ip}?"):
        isolate_host(ip)
        click.secho(f"[✓] Хост {ip} заблокирован", fg="green")

if __name__ == "__main__":
    cli()