import click

from mylib.logistics import find_coordinate, distanse, total_distanse


@click.group()
def cli():
    """Logistics command line tools."""


@cli.command()
@click.argument("city")
def coordinate(city):
    coords = find_coordinate(city)
    click.echo(f"{city}: {coords}")


@cli.command()
@click.argument("city1")
@click.argument("city2")
def distance(city1, city2):
    total = distanse(city1, city2)
    click.echo(f"Distance from {city1} to {city2}: {total:.2f} miles")


@cli.command("total-distance")
@click.argument("cities", nargs=-1)
def total_distance(cities):
    total = total_distanse(list(cities))
    click.echo(f"Total distance: {total:.2f} miles")


if __name__ == "__main__":
    cli()
