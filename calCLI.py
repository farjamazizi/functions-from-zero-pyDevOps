#!/usr/bin/env python3

from mylib.calc import add, sub, mul, div, power
import click


@click.group()
def cli():
    """A calculator program"""


@click.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_cmd(a, b):
    """Add thow numbers

    Example:
    ./calCLI.py add 1 2
    """
    click.secho(f"{a} + {b} = {add(a, b)}", fg="green")


@click.command("sub")
@click.argument("a", type=float)
@click.argument("b", type=float)
def sub_cmd(a, b):
    """Subtract two numbers

    Example:
    ./calCLI.py sub 2 1
    """
    click.secho(f"{a} - {b} = {sub(a, b)}", fg="green")


@click.command("mul")
@click.argument("a", type=float)
@click.argument("b", type=float)
def mul_cmd(a, b):
    """Multiply two numbers

    Example:
    ./calCLI.py mul 2 3
    """
    click.secho(f"{a} * {b} = {mul(a, b)}", fg="green")


@click.command("div")
@click.argument("a", type=float)
@click.argument("b", type=float)
def div_cmd(a, b):
    """Divide two numbers

    Example:
    ./calCLI.py div 6 2
    """
    click.secho(f"{a} / {b} = {div(a, b)}", fg="green")


@click.command("pow")
@click.argument("a", type=float)
@click.argument("b", type=float)
def power_cmd(a, b):
    """Raise a number to a power

    Example:
    ./calCLI.py pow 2 3
    """
    click.secho(f"{a} ** {b} = {power(a, b)}", fg="green")


cli.add_command(add_cmd)
cli.add_command(sub_cmd)
cli.add_command(mul_cmd)
cli.add_command(div_cmd)
cli.add_command(power_cmd)

if __name__ == "__main__":
    cli()
