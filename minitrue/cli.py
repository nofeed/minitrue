from pathlib import Path
from typing import Optional

import typer

app = typer.Typer()


@app.command()
def init(
    path: str = typer.Option(
        Path.cwd(),
        "--path",
        "-p",
        help="Specifies the workdir"
    )
) -> None:
    """Initializes minitrue on a given local repository (default: current)"""
    from minitrue import init
    init.inititialize(path)


def _version_callback(value: bool) -> None:
    from minitrue import APP_NAME, VERSION
    if value:
        typer.echo(f"{APP_NAME} v{VERSION}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
