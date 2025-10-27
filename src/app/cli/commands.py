import os
import pathlib

import click

from app.client.bot import Bot
from app.core import logging

logging.setup_logger()


@click.group()
def cli() -> None:
    pass


@cli.command()
def start() -> None:
    """Start client."""
    # TODO: wtf?!
    src_path = pathlib.Path(__file__).parent.parent
    src_path = pathlib.Path("src").resolve()

    os.chdir(src_path)
    #
    bot = Bot()
    bot.run()
