import asyncio
import pathlib
from collections.abc import Callable
from typing import Any, Callable

import click

from app.bot import bot as _tgbot


def common_command_options(func: Callable[..., Any]) -> Callable[..., Any]:
    func = click.option(
        "--config",
        "-c",
        type=click.Path(dir_okay=False, path_type=pathlib.Path),
        default="config.yml",
        help="Path to config file. Defaults to config.yml.",
    )(func)
    return click.pass_context(func)


@click.group()
def cli() -> None:
    pass


@cli.group()
def run() -> None:
    """Run application components."""
    pass


@run.command()
@common_command_options
def bot(ctx: click.Context, config: pathlib.Path) -> None:
    """Run bot application."""
    asyncio.run(_tgbot.run(config))
