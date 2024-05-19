"""
Module containing the CLI app of the library
"""
from typing import List
import click
from .dog import Dog


@click.group()
def cli():
    pass


@cli.command(name="hello")
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """
    Greets NAME for a total of COUNT times.

    Arguments
    ---------
    count : int
        Number of greetings.
    name : str
        The person to greet.
    """
    for x in range(count):
        click.echo(f"Hello {name}!")


@cli.command(name="bark")
@click.option("--loud", is_flag=True, show_default=True, default=False, help="let the dog bark!")
@click.option("-f", "--friend", multiple=True, default=[], help="let the dog bark!")
def bark(loud: bool, friend: List[str]):
    """
    Let the dogs out!
    
    Arguments
    ---------
    loud : bool
        Let the dog bark loud.
    friend : List[str]
        List of friends of the dog.
    """
    coco = Dog(name="Coco", friends=friend)
    click.echo(coco.bark(loud=loud))


if __name__ == "__main__":
    cli()
