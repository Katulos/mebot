import os
import pathlib
from collections.abc import Callable
from typing import Any

import click

from app.client.bot import Bot
from app.core import logging

logging.setup_logger()


@click.group()
def cli() -> None:
    pass


@cli.group()
def run() -> None:
    """Run application components."""
    pass


@run.command()
def bot(ctx: click.Context, config: pathlib.Path) -> None:
    """Run bot application."""
    # TODO: wtf?!
    src_path = pathlib.Path(__file__).parent.parent
    src_path = pathlib.Path("src").resolve()

    os.chdir(src_path)
    #
    bot = Bot()
    bot.run()
